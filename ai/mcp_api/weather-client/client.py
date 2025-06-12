import asyncio
import os
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

# Get API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Check if weather API key is set
if not WEATHER_API_KEY:
    print("WARNING: WEATHER_API_KEY not found in .env file")
    print("The weather service requires an API key for authentication")

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.openai = OpenAI()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    def _auth_error_occurred(self, final_text: list) -> bool:
        """Check if an authentication error occurred during tool calls"""
        for text in final_text:
            if isinstance(text, str) and "AUTHENTICATION ERROR" in text:
                return True
        return False
        
    async def process_query(self, query: str) -> str:
        """Process a query using OpenAI and available tools"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.inputSchema
            }
        } for tool in response.tools]

        # Initial OpenAI API call
        response = self.openai.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=1000,
            messages=messages,
            tools=available_tools
        )

        # Process response and handle tool calls
        final_text = []
        assistant_message = response.choices[0].message

        if assistant_message.content:
            final_text.append(assistant_message.content)

        # Handle tool calls
        if assistant_message.tool_calls:
            messages.append({
                "role": "assistant",
                "content": assistant_message.content,
                "tool_calls": assistant_message.tool_calls
            })

            for tool_call in assistant_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = eval(tool_call.function.arguments)  # Parse JSON string to dict
                
                # Add API key to tool args
                if WEATHER_API_KEY:
                    tool_args["api_key"] = WEATHER_API_KEY
                else:
                    final_text.append("[WARNING: No API key provided. Authentication will fail.]")
                
                # For display purposes, don't show the API key in the UI
                display_args = tool_args.copy()
                if "api_key" in display_args:
                    display_args["api_key"] = "********"

                # Execute tool call
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[Calling tool {tool_name} with args {display_args}]")
                
                # Check for authentication errors
                result_content = str(result.content)
                
                # Format for display to user with clear error message
                if result_content.startswith("ERROR:"):
                    # Create a user-friendly error message
                    if "API key" in result_content or "Authentication" in result_content or "Unauthorized" in result_content:
                        error_message = f"[⚠️ AUTHENTICATION ERROR: API key validation failed. Please check your WEATHER_API_KEY in .env file]"
                    else:
                        error_message = f"[⚠️ {result_content}]"
                    
                    # Add to display text with clear separation
                    final_text.append("\n" + "=" * 50)
                    final_text.append(error_message)
                    final_text.append("=" * 50)
                    
                        # Add error message to LLM context for proper handling
                    # Use a format that makes it very clear this is an error, not data
                    error_for_llm = (
                        "ERROR: AUTHENTICATION FAILED. Unable to retrieve weather data due to invalid API key. "
                        "This is a technical issue with the API key authentication, not a data issue. "
                        "Please inform the user that you cannot provide weather data right now due to an API key issue "
                        "and they should check their WEATHER_API_KEY configuration in the .env file."
                    )
                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": error_for_llm
                    })
                else:
                    # Add normal tool result to messages
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result_content
                    })

            # Check if an authentication error occurred
            if self._auth_error_occurred(final_text):
                # Add explicit system message about the authentication error
                messages.append({
                    "role": "system",
                    "content": (
                        "IMPORTANT: The weather data could not be retrieved due to an API KEY AUTHENTICATION ERROR. "
                        "You MUST inform the user clearly that you cannot provide weather data because of a technical issue "
                        "with API authentication. Advise them to check their WEATHER_API_KEY configuration in the .env file. "
                        "DO NOT attempt to provide generic weather information as if nothing went wrong."
                    )
                })
            
            # Get next response from OpenAI
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=1000,
                messages=messages,
            )

            if response.choices[0].message.content:
                # For authentication errors, ensure the message is clear
                if self._auth_error_occurred(final_text):
                    final_text.append("\nResponse from assistant:")
                
                final_text.append(response.choices[0].message.content)

        return "\n".join(final_text)

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
