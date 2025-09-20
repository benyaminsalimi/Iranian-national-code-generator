"""Iranian National Code Generator Module."""

import json
import importlib.resources
from typing import List, Dict, Any, Generator

from .validator import (
    validate_national_code,
    validate_city_code,
    validate_state,
    get_city_info as get_city_info_validator,
    get_available_states as get_available_states_validator,
    get_cities_by_state as get_cities_by_state_validator,
    get_all_cities as get_all_cities_validator
)
from .exceptions import CityNotFoundError, StateNotFoundError


class IranianNationalCodeGenerator:
    """
    A generator for Iranian national codes (social security numbers).

    This class provides functionality to generate and validate Iranian national codes
    based on city codes and state information.

    Attributes:
        city_codes: Dictionary mapping city codes to state and city information

    Example:
        >>> generator = IranianNationalCodeGenerator()
        >>> generator.validate("0123456789")
        True
        >>> codes = list(generator.generate_by_state("تهران"))
        >>> len(codes) > 0
        True
    """

    def __init__(self):
        """Initialize the generator with city codes data."""
        self.city_codes = self._load_city_codes()

    def _load_city_codes(self) -> Dict[str, List[str]]:
        """Load city codes from the data file."""
        try:
            # Try Python 3.9+ importlib.resources
            files = importlib.resources.files(__package__)
            data_dir = files / "data"
            with importlib.resources.as_file(data_dir / "city_codes.json") as city_file:
                with open(city_file, encoding='utf-8') as f:
                    return json.load(f)
        except AttributeError:
            # Fallback for Python < 3.9
            with importlib.resources.open_text(__package__, "data/city_codes.json") as city_file:
                return json.load(city_file)

    def validate(self, code: str) -> bool:
        """
        Validate an Iranian national code.

        Args:
            code: The 10-digit national code to validate

        Returns:
            True if the code is valid, False otherwise
        """
        return validate_national_code(code)

    def generate_all(self) -> Generator[str, None, None]:
        """
        Generate all possible valid Iranian national codes.

        Yields:
            Valid national codes one by one

        Note:
            This method can be computationally expensive as it generates
            codes for all city codes. Use it with caution or limit the results.

        Example:
            >>> generator = IranianNationalCodeGenerator()
            >>> codes = list(generator.generate_all())
            >>> len(codes) > 0
            True
        """
        for city_code in self.city_codes:
            # Generate codes for this city (0000000 to 9999999)
            for suffix in range(10000000, 19999999):
                code = str(city_code + str(suffix)[1:])
                if self.validate(code):
                    yield code

    def generate_by_state(self, target_state: str) -> Generator[str, None, None]:
        """
        Generate all valid national codes for a specific state.

        Args:
            target_state: Name of the state in Persian

        Yields:
            Valid national codes for the specified state

        Raises:
            StateNotFoundError: If the state is not found

        Example:
            >>> generator = IranianNationalCodeGenerator()
            >>> codes = list(generator.generate_by_state("تهران"))
            >>> len(codes) > 0
            True
        """
        # Check if state exists
        if not validate_state(target_state, self.city_codes):
            raise StateNotFoundError(target_state)

        for city_code in self.city_codes:
            if target_state == self.city_codes[city_code][0]:
                # Generate codes for this city
                for suffix in range(10000000, 19999999):
                    code = str(city_code + str(suffix)[1:])
                    if self.validate(code):
                        yield code

    def generate_by_city_code(self, city_code: str) -> Generator[str, None, None]:
        """
        Generate all valid national codes for a specific city code.

        Args:
            city_code: The 3-digit city code

        Yields:
            Valid national codes for the specified city code

        Raises:
            CityNotFoundError: If the city code is not found

        Example:
            >>> generator = IranianNationalCodeGenerator()
            >>> codes = list(generator.generate_by_city_code("001"))
            >>> len(codes) > 0
            True
        """
        if not validate_city_code(city_code, self.city_codes):
            raise CityNotFoundError(city_code)

        for suffix in range(10000000, 19999999):
            code = str(city_code + str(suffix)[1:])
            if self.validate(code):
                yield code

    def get_city_info(self, city_code: str) -> Dict[str, Any]:
        """
        Get information about a city code.

        Args:
            city_code: The 3-digit city code

        Returns:
            Dictionary with state and city information

        Raises:
            CityNotFoundError: If the city code is not found
        """
        try:
            return get_city_info_validator(city_code, self.city_codes)
        except ValueError as e:
            raise CityNotFoundError(city_code) from e

    def get_available_states(self) -> List[str]:
        """
        Get list of all available states.

        Returns:
            List of unique state names
        """
        return get_available_states_validator(self.city_codes)

    def get_cities_by_state(self, state: str) -> List[Dict[str, Any]]:
        """
        Get all cities for a specific state.

        Args:
            state: Name of the state

        Returns:
            List of city information dictionaries

        Raises:
            StateNotFoundError: If the state is not found
        """
        try:
            return get_cities_by_state_validator(state, self.city_codes)
        except ValueError as e:
            raise StateNotFoundError(state) from e

    def get_all_cities(self) -> List[Dict[str, Any]]:
        """
        Get all cities with their information.

        Returns:
            List of all city information dictionaries
        """
        return get_all_cities_validator(self.city_codes)