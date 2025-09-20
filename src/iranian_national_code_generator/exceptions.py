"""Custom exceptions for Iranian National Code Generator."""


class IranianNationalCodeError(Exception):
    """Base exception for Iranian National Code Generator errors."""
    pass


class CityNotFoundError(IranianNationalCodeError):
    """Raised when a city code is not found."""

    def __init__(self, city_code: str):
        self.city_code = city_code
        super().__init__(f"City code '{city_code}' not found")


class StateNotFoundError(IranianNationalCodeError):
    """Raised when a state is not found."""

    def __init__(self, state: str):
        self.state = state
        super().__init__(f"State '{state}' not found")


class InvalidNationalCodeError(IranianNationalCodeError):
    """Raised when a national code is invalid."""

    def __init__(self, code: str, reason: str = "Invalid format or checksum"):
        self.code = code
        self.reason = reason
        super().__init__(f"Invalid national code '{code}': {reason}")


class ValidationError(IranianNationalCodeError):
    """Raised when validation fails."""

    def __init__(self, message: str):
        super().__init__(message)