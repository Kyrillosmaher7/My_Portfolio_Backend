class AppException(Exception):
    def __init__(self, message: str, code: int = 400, errors: list[str] = None):
        self.message = message
        self.code = code
        self.errors = errors or []