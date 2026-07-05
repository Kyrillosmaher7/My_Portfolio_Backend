from passlib.context import CryptContext
from passlib.exc import UnknownHashError


class PasswordService:
    """
    Production-ready password hashing service using Argon2.
    """

    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["argon2"],
            deprecated="auto",
            argon2__memory_cost=65536,   # 64 MB
            argon2__time_cost=3,         # iterations
            argon2__parallelism=2        # threads
        )

    def hash_password(self, password: str) -> str:
        """
        Hash a plain password securely.
        """
        self._validate_password(password)
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, password_hash: str) -> bool:
        """
        Verify a password against a stored hash.
        """
        try:
            return self.pwd_context.verify(plain_password, password_hash)
        except UnknownHashError:
            return False

    def needs_update(self, password_hash: str) -> bool:
        """
        Check if a hash should be upgraded (useful for future migrations).
        """
        return self.pwd_context.needs_update(password_hash)

    def _validate_password(self, password: str) -> None:
        """
        Basic security rules before hashing.
        """
        if not password:
            raise ValueError("Password cannot be empty")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if len(password.encode("utf-8")) > 512:
            raise ValueError("Password is too large")