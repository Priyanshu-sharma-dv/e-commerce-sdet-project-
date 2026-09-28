from .base_client import BaseAPIClient


class AuthClient(BaseAPIClient):
    def login(self, email: str, password: str):
        return self.post("/auth/login", json={"email": email, "password": password})

    def login_and_set_token(self, email: str, password: str) -> dict:
        response = self.login(email, password)
        response.raise_for_status()
        payload = response.json()
        self.token = payload["token"]
        return payload
