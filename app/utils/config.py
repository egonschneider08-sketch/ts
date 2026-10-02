import os

from dotenv import load_dotenv

load_dotenv()

DEFAULT_WEATHER_API_KEY = "a6f25cd8f1014bed8f4190102260210"
WEATHER_API_KEY = (
    os.getenv("WEATHER_API_KEY")
    or os.getenv("weather_api_key")
    or DEFAULT_WEATHER_API_KEY
)

if not WEATHER_API_KEY:
    raise ValueError("A variável WEATHER_API_KEY não foi configurada!")