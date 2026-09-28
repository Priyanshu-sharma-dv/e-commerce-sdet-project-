import pytest

@pytest.mark.integration
@pytest.mark.smoke
def test_api_to_database_order_flow(order_client, authenticated_user, first_product, db):
    response = order_client.create(authenticated_user["id"], first_product["id"], 1)
    assert response.status_code == 201
    order = response.json()

    row = db.fetch_one(
        "SELECT id, user_id, status, total FROM orders WHERE id = :id",
        {"id": order["id"]},
    )
    assert row["id"] == order["id"]
    assert row["user_id"] == authenticated_user["id"]
    assert row["status"] == "PLACED"
