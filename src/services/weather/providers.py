import aiohttp

from src.config import config
from src.logging import logger
from src.services.weather.abc import WeatherProvider


class WtrrApiClient(WeatherProvider):
    """
    Wtrr API client. It placed here for demonstration purposes and simplifying code structure.
    """

    def __init__(self, url: str, timeout: int = config.request_timeout):
        self.url = url
        self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout))


    async def get_weather(self, city: str) -> aiohttp.ClientResponse:
        logger.debug(f"Getting weather for {city} from Wtrr API")
        return await self.session.get(f"{self.url}/{city}?format=%l,%C,%t")
