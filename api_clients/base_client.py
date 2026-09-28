import httpx
from utils.logger import get_logger

logger = get_logger(__name__)


class BaseAPIClient:
    def __init__(self, base_url: str, token: str | None = None):
        self.client = httpx.Client(base_url=base_url, timeout=10)
        self.token = token

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def request(self, method: str, path: str, **kwargs) -> httpx.Response:
        headers = {**self.headers, **kwargs.pop("headers", {})}
        logger.info("%s %s", method.upper(), path)
        response = self.client.request(method, path, headers=headers, **kwargs)
        logger.info("Response: %s", response.status_code)
        return response

    def get(self, path, **kwargs): return self.request("GET", path, **kwargs)
    def post(self, path, **kwargs): return self.request("POST", path, **kwargs)
    def put(self, path, **kwargs): return self.request("PUT", path, **kwargs)
    def delete(self, path, **kwargs): return self.request("DELETE", path, **kwargs)

    def close(self):
        self.client.close()
