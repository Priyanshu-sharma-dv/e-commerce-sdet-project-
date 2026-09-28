import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_product_search(product_client):
    response = product_client.list(query="Laptop")
    assert response.status_code == 200
    assert any(product["name"] == "Laptop Pro" for product in response.json())

@pytest.mark.api
@pytest.mark.parametrize("product_id, expected_status", [(999999, 404), (1, 200)])
def test_get_product(product_client, product_id, expected_status):
    response = product_client.get_by_id(product_id)
    assert response.status_code == expected_status
