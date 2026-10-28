import pytest

from main import httpServer


@pytest.mark.parametrize("path", ["/health", "/health/"])
def test_health_returns_healthy(path):
    client = httpServer.test_client()

    response = client.get(path)

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
