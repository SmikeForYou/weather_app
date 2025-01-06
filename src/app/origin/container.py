from dependency_injector import containers, providers

from src.config import config
from src.services.weather.providers import WtrrApiClient
from src.services.weather.service import WeatherService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])
    wttr_api_client = providers.Factory(WtrrApiClient, url=config.wtrr_api_url)
    weather_service = providers.Factory(WeatherService, weather_provider=wttr_api_client)
