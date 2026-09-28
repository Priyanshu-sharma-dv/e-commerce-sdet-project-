import pytest
from api_clients.schemas import OrderResponse
from utils.config import settings


@pytest.mark.integration
@pytest.mark.regression
def test_create_order_response_contract(authenticated_client, first_product):
    payload = {
        "user_id": authenticated_client.login_and_set_token(settings.test_email, settings.test_password)["user"]["id"],
        "items": [{"product_id": first_product["id"], "quantity": 1}],
    }
    response = authenticated_client.post("/orders", json=payload)
    assert response.status_code == 201
    order = OrderResponse.model_validate(response.json())
    assert order.total >= 0
    assert order.status
