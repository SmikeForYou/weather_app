from unittest import mock
import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from src.app.proxy.app import app as proxy_app
from src.app.origin.app import app as origin_app
from  src.services.weather.providers import WtrrApiClient
from src.services.origin.providers import OriginServerClient
from src.services.cache.containers import WeatherContainer

@pytest.fixture(autouse=True)
def weather_client_mock():
    wtrr_client_mock = mock.AsyncMock(spec=WtrrApiClient)
    wtrr_client_mock.get_weather.return_value = mock.MagicMock()
    wtrr_client_mock.return_value.ok = True

    async def mock_text():
        return "Kharkiv,Cloudy,10"

    wtrr_client_mock.get_weather.return_value.text = mock_text
    origin_app.container.wttr_api_client.override(wtrr_client_mock)


@pytest.fixture
def origin_client():
    with TestClient(origin_app) as client:
        yield client


@pytest.fixture(autouse=True)
def mock_proxy_client(origin_client, weather_client_mock):
    origin_server_client_mock = mock.AsyncMock(spec=OriginServerClient)

    async def mock_json():
        return origin_client.get("/weather/Kharkiv").json()

    origin_server_client_mock.get_weather.return_value.json = mock_json
    origin_server_client_mock.get_weather.return_value.ok = True
    proxy_app.container.weather_container.origin_server_client.override(origin_server_client_mock)



@pytest.fixture
def proxy_client():
    return AsyncClient(
        transport=ASGITransport(app=proxy_app),
        base_url="http://test_proxy",
    )


@pytest.mark.asyncio
async def test_get_weather_without_cache(proxy_client):
    response_1 = await proxy_client.post("/weather/", json={"city": "Kharkiv"}, headers={"Cache-Control": "no-cache"})
    assert response_1.status_code == 200
    response_1_json = response_1.json()
    assert response_1_json["city"] == "Kharkiv"
    assert response_1_json["temperature"] == "10"
    assert response_1_json["weather"] == "Cloudy"
    response_2 = await proxy_client.post("/weather/", json={"city": "Kharkiv"}, headers={"Cache-Control": "no-cache"})
    assert response_2.status_code == 200
    response_2_json = response_1.json()
    assert response_2_json["city"] == "Kharkiv"
    assert response_2_json["temperature"] == "10"
    assert response_2_json["weather"] == "Cloudy"
    assert response_1.json()["timestamp"] != response_2.json()["timestamp"]




@pytest.mark.asyncio
async def test_get_cached_weather(proxy_client):
    response_1 = await proxy_client.post("/weather/", json={"city": "Kharkiv"})
    assert response_1.status_code == 200
    response_1_json = response_1.json()
    assert response_1_json["city"] == "Kharkiv"
    assert response_1_json["temperature"] == "10"
    assert response_1_json["weather"] == "Cloudy"
    response_2 = await proxy_client.post("/weather/", json={"city": "Kharkiv"})
    assert response_2.status_code == 200
    response_2_json = response_1.json()
    assert response_2_json["city"] == "Kharkiv"
    assert response_2_json["temperature"] == "10"
    assert response_2_json["weather"] == "Cloudy"
    assert response_1.json()["timestamp"] == response_2.json()["timestamp"]



