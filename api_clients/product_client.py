from .base_client import BaseAPIClient

class ProductClient(BaseAPIClient):
    def list(self, query: str | None = None, category: str | None = None):
        params = {k: v for k, v in {"q": query, "category": category}.items() if v}
        return self.get("/products", params=params)

    def get_by_id(self, product_id: int):
        return self.get(f"/products/{product_id}")
