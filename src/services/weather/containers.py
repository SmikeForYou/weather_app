from dependency_injector import containers, providers

from src.config import config

from .providers import WtrrApiClient
from .service import WeatherService


class WeatherContainer(containers.DeclarativeContainer):
    wttr_api_client = providers.Factory(WtrrApiClient, url=config.wtrr_api_url)
    weather_service = providers.Factory(WeatherService, weather_provider=wttr_api_client)
