from dependency_injector import containers, providers

from src.config import config
from src.services.cache.manager import WeatherManager
from src.services.cache.service import WeatherCacheService
from src.services.origin.providers import OriginServerClient
from src.services.origin.service import OriginService


class WeatherContainer(containers.DeclarativeContainer):
    origin_server_client = providers.Factory(OriginServerClient, base_url=config.origin_server_url)
    origin_service = providers.Factory(OriginService, origin_client=origin_server_client)
    cache = providers.Singleton(WeatherCacheService)
    weather_manager = providers.Factory(WeatherManager, cache=cache, origin=origin_service)