from dataclasses import dataclass


@dataclass(frozen=True)
class AuthContext:
    token: str
    user_id: int
    email: str
