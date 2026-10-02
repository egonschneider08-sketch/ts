import importlib


def test_config_uses_weather_api_key_env(monkeypatch):
    monkeypatch.setenv("WEATHER_API_KEY", "test_key")
    import app.utils.config as config

    importlib.reload(config)

    assert config.WEATHER_API_KEY == "test_key"


def test_weather_api_does_not_prompt_for_city(monkeypatch):
    import builtins

    def fail_input(*args, **kwargs):
        raise AssertionError("input() should not be called when importing the module")

    monkeypatch.setattr(builtins, "input", fail_input)

    import app.services.weather_api as weather_api

    importlib.reload(weather_api)

    assert callable(weather_api.get_weather)
