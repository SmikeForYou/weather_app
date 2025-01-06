import json

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Request

from src.services.cache.manager import WeatherManager
from .schemas import WeatherResponse, WeatherRequest
from .container import Container
router = APIRouter()


@router.post("/weather/", response_model=WeatherResponse)
@inject
async def weather(
    request: Request,
    body: WeatherRequest,
    weather_service: WeatherManager = Depends(
        Provide[Container.weather_service]
    ),
):
    use_cache = request.headers.get("Cache-Control") != "no-cache"
    weather_data = await weather_service.get_weather(body.city, use_cache)
    return WeatherResponse(
        city=weather_data.city,
        temperature=weather_data.temperature,
        weather=weather_data.weather,
        timestamp=weather_data.timestamp.isoformat(),
    )