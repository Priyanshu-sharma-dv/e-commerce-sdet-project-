from .base_client import BaseAPIClient

class OrderClient(BaseAPIClient):
    def create(self, user_id: int, product_id: int, quantity: int = 1):
        return self.post("/orders", json={"user_id": user_id, "items": [{"product_id": product_id, "quantity": quantity}]})

    def get_by_id(self, order_id: int):
        return self.get(f"/orders/{order_id}")
