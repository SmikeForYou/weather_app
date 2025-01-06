from src.exceptions.base import OriginClientException
from src.services.origin.providers import OriginServerClient
from src.services.origin.dto import WeatherResponse


class OriginService:
    def __init__(self, origin_client: OriginServerClient):
        self.origin_client = origin_client

    async def get_weather(self, city: str) -> WeatherResponse:
        response = await self.origin_client.get_weather(city)
        if not response.ok:
            text_ = await response.text()
            raise OriginClientException(f"Failed to get weather for {city}. Status code: {response.status}. Reason: {text_}")
        json_ = await response.json()
        return WeatherResponse(**json_)