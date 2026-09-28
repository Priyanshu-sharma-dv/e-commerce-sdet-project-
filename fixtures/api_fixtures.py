import pytest
from api_clients.auth_client import AuthClient
from api_clients.product_client import ProductClient
from api_clients.order_client import OrderClient
from utils.config import settings


@pytest.fixture

def auth_client():
    client = AuthClient(settings.api_url)
    yield client
    client.close()


@pytest.fixture

def product_client():
    client = ProductClient(settings.api_url)
    yield client
    client.close()


@pytest.fixture

def authenticated_client(auth_client):
    auth_client.login_and_set_token(settings.test_email, settings.test_password)
    return auth_client


@pytest.fixture

def order_client(authenticated_client):
    client = OrderClient(settings.api_url, token=authenticated_client.token)
    yield client
    client.close()
