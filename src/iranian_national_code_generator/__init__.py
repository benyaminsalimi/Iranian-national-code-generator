"""Iranian National Code Generator - A Python library for generating and validating Iranian national codes."""

__version__ = "1.0.0"
__author__ = "Benyamin Salimi"
__email__ = "Benyamin.Salimi@gmail.com"
__license__ = "MIT"

from .generator import IranianNationalCodeGenerator
from .validator import (
    validate_national_code,
    is_valid_format,
    validate_city_code,
    validate_state,
    get_city_info,
    get_available_states,
    get_cities_by_state,
    get_all_cities,
)
from .exceptions import (
    IranianNationalCodeError,
    CityNotFoundError,
    StateNotFoundError,
    InvalidNationalCodeError,
    ValidationError,
)

__all__ = [
    "IranianNationalCodeGenerator",
    "validate_national_code",
    "is_valid_format",
    "validate_city_code",
    "validate_state",
    "get_city_info",
    "get_available_states",
    "get_cities_by_state",
    "get_all_cities",
    "IranianNationalCodeError",
    "CityNotFoundError",
    "StateNotFoundError",
    "InvalidNationalCodeError",
    "ValidationError",
]