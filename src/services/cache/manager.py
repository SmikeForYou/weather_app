import datetime

from src.services.cache.dto import Weather
from src.services.cache.service import WeatherCacheService
from src.services.origin.service import OriginService


class WeatherManager:
    def __init__(self, cache: WeatherCacheService, origin: OriginService):
        self.cache = cache
        self.origin = origin

    async def get_weather(self, city: str, use_cache: bool = True) -> Weather:
        if use_cache:
            cached_weather = self.cache.get(city)
            if cached_weather is not None:
                return cached_weather

        weather_response = await self.origin.get_weather(city)
        timestamp = datetime.datetime.now()
        weather = Weather(
                city=weather_response.city,
                temperature=weather_response.temperature,
                weather=weather_response.weather,
                timestamp=timestamp,
            )
        self.cache.set(
            city, weather
        )
        return weather
