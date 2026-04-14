import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_version_endpoint(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert 'TempBox' in response.json['app']

def test_temperature_endpoint(client):
    response = client.get('/temperature')
    assert response.status_code in [200, 503]
