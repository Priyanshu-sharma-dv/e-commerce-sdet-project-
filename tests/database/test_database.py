import pytest

@pytest.mark.db
@pytest.mark.smoke
def test_seeded_product_exists(db):
    row = db.fetch_one("SELECT id, name, stock FROM products WHERE name = :name", {"name": "Laptop Pro"})
    assert row is not None
    assert row["stock"] >= 0

@pytest.mark.db
def test_order_can_be_found_after_creation(db, order_client, authenticated_user, first_product):
    response = order_client.create(authenticated_user["id"], first_product["id"], 1)
    assert response.status_code == 201
    order_id = response.json()["id"]
    row = db.fetch_one("SELECT id, user_id, status FROM orders WHERE id = :id", {"id": order_id})
    assert row == {"id": order_id, "user_id": authenticated_user["id"], "status": "PLACED"}
