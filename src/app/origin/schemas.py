from pydantic import BaseModel


class WeatherResponse(BaseModel):
    city: str
    temperature: str
    weather: str