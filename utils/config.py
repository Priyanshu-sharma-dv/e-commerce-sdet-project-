import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "http://localhost:8000")
    api_url: str = os.getenv("API_URL", "http://localhost:8000/api")
    database_url: str = os.getenv("DATABASE_URL", "postgresql+psycopg://ecommerce:ecommerce@localhost:5432/ecommerce")
    test_email: str = os.getenv("TEST_EMAIL", "qa@example.com")
    test_password: str = os.getenv("TEST_PASSWORD", "Password123")
    screenshot_on_failure: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

settings = Settings()
