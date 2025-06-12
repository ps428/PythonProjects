# Weather App with Model Context Protocol

A simple yet powerful weather application that demonstrates using Model Context Protocol (MCP) with OpenAI.

## What Is This Project?

This project showcases how to build an AI application with specialized capabilities by connecting an LLM (OpenAI's GPT-4o-mini) to custom tools. The app allows users to get real-time weather information by:

- Checking weather forecasts for any location (in USA)
- Getting active weather alerts by state
- Interacting through natural language queries

## How It Works

The project follows a client-server architecture:

### Weather Client
- **User Interface**: Provides a simple text-based chat interface
- **OpenAI Integration**: Sends user queries to GPT-4o-mini
- **MCP Implementation**: Detects when the AI needs weather data and connects to the server
- **Tool Management**: Handles the tool calling lifecycle and presents results back to the user

### Weather Server
- **Weather API Integration**: Connects to the National Weather Service (NWS) API
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

   Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Server Setup**:
   ```
   cd weather-server
   pip install -e .
   ```

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
- **Error Handling**: Gracefully manages API timeouts and connection issues
- **Extensible Design**: Easily add more weather tools or connect to different APIs

## Learn More

This project demonstrates practical usage of the Model Context Protocol. To learn more:
- [MCP Documentation](https://modelcontextprotocol.io/introduction)
- [National Weather Service API](https://weather-gov.github.io/api/)
