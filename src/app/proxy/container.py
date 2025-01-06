from dependency_injector import containers, providers

from src.services.cache import containers as cache_containers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])
    weather_container = providers.Container(cache_containers.WeatherContainer)
    weather_service = providers.Factory(weather_container.weather_manager)