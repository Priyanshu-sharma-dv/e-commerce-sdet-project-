import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_create_and_get_order(order_client, authenticated_user, first_product):
    create = order_client.create(authenticated_user["id"], first_product["id"], 1)
    assert create.status_code == 201
    order = create.json()
    assert order["status"] == "PLACED"
    assert order["total"] > 0

    get_response = order_client.get_by_id(order["id"])
    assert get_response.status_code == 200
    assert get_response.json()["id"] == order["id"]

@pytest.mark.api
@pytest.mark.parametrize("quantity, expected_status", [(0, 422), (21, 422)])
def test_invalid_order_quantity(order_client, authenticated_user, first_product, quantity, expected_status):
    response = order_client.create(authenticated_user["id"], first_product["id"], quantity)
    assert response.status_code == expected_status
