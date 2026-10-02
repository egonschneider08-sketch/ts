import requests

from app.utils.config import WEATHER_API_KEY

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> dict:
    if not city or not city.strip():
        raise ValueError("Informe uma cidade válida.")

    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "lang": "pt",
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10,
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Erro ao consultar a API. "
            f"Status: {response.status_code}"
        )

    return response.json()