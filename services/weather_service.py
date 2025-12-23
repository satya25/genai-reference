import requests

class WeatherService:
    """
    Simple service to fetch local weather using Open-Meteo API
    """
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude: float, longitude: float):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            weather = data.get("current_weather", {})
            if weather:
                return f"{weather['temperature']}°C, Wind {weather['windspeed']} km/h, Weather code {weather['weathercode']}"
            else:
                return "Weather data not available."
        except Exception as e:
            return f"[Weather Error] {str(e)}"
