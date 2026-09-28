import pytest
from utils.config import settings

@pytest.mark.api
@pytest.mark.smoke
def test_valid_login(auth_client):
    response = auth_client.login(settings.test_email, settings.test_password)
    assert response.status_code == 200
    assert response.json()["user"]["email"] == settings.test_email
    assert response.json()["token"]

@pytest.mark.api
@pytest.mark.parametrize("password", ["wrong", "", "Password1234"])
def test_invalid_login(auth_client, password):
    response = auth_client.login(settings.test_email, password)
    assert response.status_code == 401
