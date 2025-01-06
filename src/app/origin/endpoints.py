import json

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.services.weather import service as weather_services

from .container import Container
from .schemas import WeatherResponse

router = APIRouter()


@router.get("/weather/{city}/", response_model=WeatherResponse)
@inject
async def weather(
    city: str,
    weather_service: weather_services.WeatherService = Depends(
        Provide[Container.weather_service]
    ),
):
    weather_data = await weather_service.get_weather(city)
    return WeatherResponse(
        city=weather_data.city,
        temperature=weather_data.temperature,
        weather=weather_data.weather,
    )