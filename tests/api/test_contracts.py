import pytest
from api_clients.schemas import LoginResponse, ProductResponse
from utils.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_login_response_contract(auth_client):
    response = auth_client.login(settings.test_email, settings.test_password)
    assert response.status_code == 200
    model = LoginResponse.model_validate(response.json())
    assert model.user.email == settings.test_email


@pytest.mark.api
@pytest.mark.regression
def test_product_response_contract(product_client):
    response = product_client.list()
    assert response.status_code == 200
    products = [ProductResponse.model_validate(item) for item in response.json()]
    assert products
    assert all(item.price >= 0 for item in products)
