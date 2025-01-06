from unittest import mock
import pytest

from src.services.weather.providers import WtrrApiClient
from src.services.weather.containers import WeatherContainer
from src.exceptions.base import WeatherProviderException

@pytest.mark.asyncio
async def test_get_weather_by_city_happy_path():
    wtrr_client_mock = mock.AsyncMock(spec=WtrrApiClient)
    wtrr_client_mock.get_weather.return_value = mock.MagicMock()
    wtrr_client_mock.get_weather.return_value.ok = True

    async def mock_text():
        return "Kharkiv,Cloudy,10"

    wtrr_client_mock.get_weather.return_value.text = mock_text
    container = WeatherContainer()
    container.wttr_api_client.override(wtrr_client_mock)
    weather_service = container.weather_service()
    weather = await weather_service.get_weather("Kharkiv")
    assert weather.city == "Kharkiv"
    assert weather.temperature == '10'
    assert weather.weather == "Cloudy"


@pytest.mark.asyncio
async def test_get_weather_by_city_unhappy_path():
    wtrr_client_mock = mock.AsyncMock(spec=WtrrApiClient)
    wtrr_client_mock.get_weather.return_value = mock.MagicMock()
    wtrr_client_mock.get_weather.return_value.ok = False

    async def mock_text():
        return "Kharkiv,Cloudy,10"

    wtrr_client_mock.get_weather.return_value.text = mock_text
    container = WeatherContainer()
    container.wttr_api_client.override(wtrr_client_mock)
    weather_service = container.weather_service()
    with pytest.raises(WeatherProviderException):
        await weather_service.get_weather("Kharkiv")