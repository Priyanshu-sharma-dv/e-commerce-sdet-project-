import pytest
from utils.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_protected_order_endpoint_rejects_missing_token(product_client):
    response = product_client.get("/orders/1")
    assert response.status_code in (401, 403, 404)


@pytest.mark.api
@pytest.mark.smoke
def test_authenticated_client_can_access_order(authenticated_client):
    response = authenticated_client.get("/orders/1")
    assert response.status_code in (200, 404)
