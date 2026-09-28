import os
import httpx

class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("API_URL", "http://localhost:8000/api")
        self.client = httpx.Client(base_url=self.base_url, timeout=10)

    def get(self, path, **kwargs): return self.client.get(path, **kwargs)
    def post(self, path, **kwargs): return self.client.post(path, **kwargs)
    def close(self): self.client.close()
