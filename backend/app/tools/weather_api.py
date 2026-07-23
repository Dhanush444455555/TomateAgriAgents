"""Weather API Tool - Fetches real-time weather data for agent reasoning."""
import httpx
from app.config import settings


class WeatherAPITool:
    """Fetches weather data from OpenWeatherMap / IMD API.
    
    Used by: WeatherAgent, SoilIrrigationAgent, PestRiskAgent
    Returns structured weather data including forecasts.
    """
    
    name = "weather_api"
    description = "Fetch current weather and 7-day forecast for a given location (lat/lon)"
    
    async def execute(self, lat: float, lon: float) -> dict:
        """Fetch weather data from OpenWeatherMap API."""
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": settings.WEATHER_API_KEY,
            "units": "metric"
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                return {
                    "success": True,
                    "current": {
                        "temperature": data["list"][0]["main"]["temp"],
                        "humidity": data["list"][0]["main"]["humidity"],
                        "wind_speed": data["list"][0]["wind"]["speed"],
                        "description": data["list"][0]["weather"][0]["description"],
                        "rain_mm": data["list"][0].get("rain", {}).get("3h", 0),
                    },
                    "forecast": [
                        {
                            "datetime": item["dt_txt"],
                            "temp": item["main"]["temp"],
                            "humidity": item["main"]["humidity"],
                            "rain_mm": item.get("rain", {}).get("3h", 0),
                            "description": item["weather"][0]["description"],
                        }
                        for item in data["list"][:16]  # Next 48 hours
                    ],
                    "source": "OpenWeatherMap API"
                }
        except Exception as e:
            return {"success": False, "error": str(e), "source": "OpenWeatherMap API"}
