from typing import Any
import httpx
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import secrets

# Load environment variables
load_dotenv()

# Get API key from environment or generate a secure one if not present
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    # Generate a random API key if not set
    API_KEY = secrets.token_hex(16)
    print(f"WARNING: No API key found in environment. Generated temporary key: {API_KEY}")
    print("Set this key in both server and client .env files as WEATHER_API_KEY")

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


def verify_api_key(api_key: str) -> bool:
    """Verify that the provided API key is valid.
    
    This is a simple mock of API key validation that just checks against 
    a predefined value. In a production system, this would typically involve
    checking against a database of valid keys with proper hashing.
    """
    # For demonstration purposes, we also accept empty keys if no key was set in env
    if not API_KEY and not api_key:
        print("[SECURITY] No API key was configured, accepting empty key")
        return True
        
    is_valid = api_key == API_KEY
    return is_valid

async def make_nws_request(url: str, api_key: str = None) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling.
    
    Args:
        url: The NWS API URL to request
        api_key: API key for authentication (validated but not forwarded)
    """
    # Verify API key before making any request
    if not verify_api_key(api_key):
        print(f"[SECURITY] API request rejected - Invalid API key provided")
        return {
            "error": "Authentication failed", 
            "message": "Unauthorized: Invalid API key. Please check your WEATHER_API_KEY configuration."
        }
    
    # Log successful authentication
    print(f"[SECURITY] API request authorized with valid API key")
        
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    # API key is not passed to the actual NWS API
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Failed to fetch data: {str(e)}"}


def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""


@mcp.tool()
async def get_alerts(state: str, api_key: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
        api_key: API key for authentication
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url, api_key)

    # Check for authentication error
    if isinstance(data, dict) and "error" in data:
        if "Authentication failed" in data.get("error", ""):
            return f"ERROR: {data.get('message', 'Unauthorized access')}"
        elif "message" in data:
            return f"ERROR: {data['message']}"
        else:
            return f"ERROR: {data.get('error', 'Unknown error')}"

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)


@mcp.tool()
async def get_forecast(latitude: float, longitude: float, api_key: str) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        api_key: API key for authentication
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url, api_key)
    
    # Check for authentication error
    if isinstance(points_data, dict) and "error" in points_data:
        if "Authentication failed" in points_data.get("error", ""):
            return f"ERROR: {points_data.get('message', 'Unauthorized access')}"
        elif "message" in points_data:
            return f"ERROR: {points_data['message']}"
        else:
            return f"ERROR: {points_data.get('error', 'Unknown error')}"

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url, api_key)
    
    # Check for authentication error in second request
    if isinstance(forecast_data, dict) and "error" in forecast_data:
        if "Authentication failed" in forecast_data.get("error", ""):
            return f"ERROR: {forecast_data.get('message', 'Unauthorized access')}"
        elif "message" in forecast_data:
            return f"ERROR: {forecast_data['message']}"
        else:
            return f"ERROR: {forecast_data.get('error', 'Unknown error')}"

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

if __name__ == "__main__":
    # Print security information
    if API_KEY:
        print(f"[SECURITY] Server starting with API key authentication enabled")
        # Only show first few chars for security
        masked_key = API_KEY[:4] + "*" * (len(API_KEY) - 4) if len(API_KEY) > 4 else "****"
        print(f"[SECURITY] Using API key: {masked_key}")
    else:
        print("[SECURITY] WARNING: No API key configured. Server will accept empty keys.")
        print("[SECURITY] Set WEATHER_API_KEY in .env file to enable authentication.")
    
    # Initialize and run the server
    mcp.run(transport='stdio')
