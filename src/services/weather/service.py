import aiohttp

from src.config import config
from src.exceptions import WeatherProviderException
from src.logging import logger
from src.services.weather.abc import WeatherProvider
from src.services.weather.dto import WeatherResponse


class RetryProviderDecorator(WeatherProvider):
    def __init__(self, weather_provider: WeatherProvider, retries: int):
        self.weather_provider = weather_provider
        self.retries = retries

    async def get_weather(self, city: str) -> aiohttp.ClientResponse:
        for i in range(self.retries):
            response = await self.weather_provider.get_weather(city)
            if response.ok:
                return response
            logger.warning(f"Failed to get weather for {city}. Retrying...")
        raise WeatherProviderException(f"Failed to get weather for {city} after {self.retries} retries")


class WeatherService:
    def __init__(self, weather_provider: WeatherProvider):
        self.weather_provider = RetryProviderDecorator(weather_provider, retries=config.max_retries)

    async def get_weather(self, city: str) -> WeatherResponse:
        response = await self.weather_provider.get_weather(city)
        text = await response.text()
        city, weather, temperature = text.split(",", 3)
        return WeatherResponse(
            city=city,
            temperature=temperature,
            weather=weather,
        )
