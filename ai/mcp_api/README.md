# Weather App with Model Context Protocol and API Authentication

A simple yet powerful weather application that demonstrates using Model Context Protocol (MCP) with OpenAI, featuring secure API authentication between client and server.

## What Is This Project?

This project showcases how to build an AI application with specialized capabilities by connecting an LLM (OpenAI's GPT-4o-mini) to custom tools with secure API validation. The app allows users to get real-time weather information by:

- Checking weather forecasts for any location (in USA)
- Getting active weather alerts by state
- Interacting through natural language queries
- Validating API access between client and server

## How It Works

The project follows a client-server architecture with API authentication:

### Weather Client
- **User Interface**: Provides a simple text-based chat interface
- **OpenAI Integration**: Sends user queries to GPT-4o-mini
- **MCP Implementation**: Detects when the AI needs weather data and connects to the server
- **Tool Management**: Handles the tool calling lifecycle and presents results back to the user
- **API Authentication**: Sends API key with each request to the server

### Weather Server
- **Weather API Integration**: Connects to the National Weather Service (NWS) API
- **API Validation**: Verifies client API key before processing any request
- **Tool Registration**: Exposes two specialized tools:
  - `get_alerts`: Fetches active weather alerts for any US state
  - `get_forecast`: Retrieves detailed weather forecasts for specific coordinates
- **Data Processing**: Formats complex weather data into readable responses

## Setting Up the Project

### Prerequisites
- Python 3.10+
- OpenAI API key

### Installation

1. **Client Setup**:
   ```
   cd weather-client
   pip install -e .
   ```

   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   WEATHER_API_KEY=your_weather_api_key_here
   ```

2. **Server Setup**:
   ```
   cd weather-server
   pip install -e .
   ```

   Create a `.env` file with the same weather API key used in the client:
   ```
   WEATHER_API_KEY=your_weather_api_key_here
   ```

> **Security Note**: The client and server must use the same `WEATHER_API_KEY` value for authentication to succeed. If no API key is provided, the server will generate a temporary key and display it on startup. This implementation demonstrates API key validation at the MCP server level without forwarding the key to the weather API.

## Running the Application

1. Start the server:
   ```
   cd weather-server
   python weather.py
   ```

2. In a new terminal, start the client:
   ```
   cd weather-client
   python client.py ../weather-server/weather.py
   ```

3. Start asking about the weather!
   - "What's the forecast for New York City?"
   - "Are there any weather alerts in California?"
   - "Will it rain tomorrow in Seattle?"

## Example Interaction

```
Query: What's the weather like in Boston?

[Calling tool get_forecast with args {'latitude': 42.3601, 'longitude': -71.0589}]

Tonight:
Temperature: 65°F
Wind: 5 to 10 mph SW
Forecast: Partly cloudy, with a low around 65. Southwest wind 5 to 10 mph.

---
Tuesday:
Temperature: 85°F
Wind: 5 to 10 mph SW
Forecast: Mostly sunny, with a high near 85. Southwest wind 5 to 10 mph.
```

## Technical Details

- **Transport Protocol**: Uses stdio for client-server communication
- **Security**: Demonstrates API key-based authentication at the MCP server level
- **Error Handling**: Gracefully manages API timeouts and connection issues
- **Extensible Design**: Easily add more weather tools or connect to different APIs

### Security Implementation Details

This project demonstrates a secure client-server architecture using API key authentication:

#### API Key Authentication Flow

1. **Key Management**:
   - Both client and server load the same API key from their respective `.env` files
   - If no key is found, the server generates a secure random key at startup
   - The server displays the generated key so it can be added to the client's configuration

2. **Client-Side Processing**:
   - The client automatically injects the API key into every tool call
   - For privacy, the client masks the API key in logs and UI output (`api_key: "********"`)
   - When tool calls fail due to authentication, the client renders prominent error messages

3. **Server-Side Verification**:
   - The server validates the API key before processing any request
   - Verification happens in the `make_nws_request` function, which all tools use
   - The API key is not forwarded to the NWS API (which is a public API)
   - Failed authentication attempts are logged for security monitoring

4. **Error Handling**:
   - Authentication failures return structured error responses
   - The server logs security events for monitoring
   - The client displays clear error messages to the user with visual separators
   - The LLM is explicitly instructed to inform users about authentication failures

5. **Security Considerations**:
   - The authentication happens at the MCP protocol level
   - This is a demonstration of the concept - production systems would use more robust auth
   - In a real-world scenario, API keys would be stored in a secure database with proper hashing

#### Authentication Error Examples

When API key authentication fails, the system provides clear error messages:

**Server-Side Logs:**
```
[SECURITY] API request rejected - Invalid API key provided
```

**Client-Side UI:**
```
[Calling tool get_forecast with args {'latitude': 28.5383, 'longitude': -81.3792, 'api_key': '********'}]

==================================================
[⚠️ AUTHENTICATION ERROR: API key validation failed. Please check your WEATHER_API_KEY in .env file]
==================================================

Response from assistant:
I'm unable to provide weather information right now due to an authentication error. Please check the WEATHER_API_KEY in your .env file to ensure it matches the server's key.
```

This clear error presentation helps users quickly identify and fix authentication issues.

#### Key Implementation Details

Here are the key code components that implement the API key authentication:

**Server-Side (weather.py):**
```python
# Load API key from environment
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    # Generate a secure key if none exists
    API_KEY = secrets.token_hex(16)
    print(f"WARNING: No API key found in environment. Generated temporary key: {API_KEY}")

def verify_api_key(api_key: str) -> bool:
    """Verify that the provided API key is valid"""
    # In production, this would check against a secure database
    return api_key == API_KEY

async def make_nws_request(url: str, api_key: str = None) -> dict[str, Any] | None:
    # Verify API key before processing request
    if not verify_api_key(api_key):
        print(f"[SECURITY] API request rejected - Invalid API key provided")
        return {"error": "Authentication failed", "message": "Unauthorized: Invalid API key"}

    # Continue with the actual API request if authentication passed
    # ...
```

**Client-Side (client.py):**
```python
# Tool call processing
tool_args = eval(tool_call.function.arguments)

# Add API key to tool args
if WEATHER_API_KEY:
    tool_args["api_key"] = WEATHER_API_KEY

# Mask API key in logs
display_args = tool_args.copy()
if "api_key" in display_args:
    display_args["api_key"] = "********"

# Execute tool call and process results
result = await self.session.call_tool(tool_name, tool_args)

# Handle authentication errors
if result_content.startswith("ERROR:"):
    # Display prominent error message
    # ...
```

This modular approach makes it easy to extend with more advanced authentication methods in the future.

## Learn More

This project demonstrates practical usage of the Model Context Protocol. To learn more:
- [MCP Documentation](https://modelcontextprotocol.io/introduction)
- [National Weather Service API](https://weather-gov.github.io/api/)
- [MCP Server](https://modelcontextprotocol.io/quickstart/server)
- [MCP Client](https://modelcontextprotocol.io/quickstart/client)
