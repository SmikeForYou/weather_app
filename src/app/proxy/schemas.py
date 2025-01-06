from pydantic import BaseModel


class WeatherRequest(BaseModel):
    city: str


class WeatherResponse(BaseModel):
    city: str
    temperature: str
    weather: str
    timestamp: str