import aiohttp
from src.config import config

class OriginServerClient:
    def __init__(self, base_url: str, timeout: int = config.request_timeout):
        self.base_url = base_url
        self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout))


    async def get_weather(self, city: str):
        return await self.session.get(f"{self.base_url}/weather/{city}")