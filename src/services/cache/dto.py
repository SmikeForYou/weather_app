import datetime

from pydantic import BaseModel


class Weather(BaseModel):
    city: str
    temperature: str
    weather: str
    timestamp: datetime.datetime


    def is_expired(self, ttl: int) -> bool:
        return (datetime.datetime.now() - self.timestamp).seconds > ttl