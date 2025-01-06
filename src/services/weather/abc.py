from abc import ABC, abstractmethod

import aiohttp


class WeatherProvider(ABC):

    @abstractmethod
    async def get_weather(self, city: str) -> aiohttp.ClientResponse:
        pass
