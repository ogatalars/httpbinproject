import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_ip(client):
    response = client.get('/ip')
    assert response.status_code == 200
    data = response.get_json()
    assert 'origin' in data