"""Iranian National Code Validation Module."""

import re
from typing import Dict, List, Any


def validate_national_code(code: str) -> bool:
    """
    Validate an Iranian national code.

    Args:
        code: The 10-digit national code to validate

    Returns:
        True if the code is valid, False otherwise

    Example:
        >>> validate_national_code("0123456789")
        True
        >>> validate_national_code("123456789")
        False
    """
    if not isinstance(code, str):
        return False

    if not re.search(r'^\d{10}$', code):
        return False

    check = int(code[9])
    s = sum([int(code[x]) * (10 - x) for x in range(9)]) % 11
    return (s < 2 and check == s) or (s >= 2 and check + s == 11)


def is_valid_format(code: str) -> bool:
    """
    Check if the code has the correct format (10 digits).

    Args:
        code: The code to check

    Returns:
        True if the format is correct, False otherwise
    """
    if not isinstance(code, str):
        return False
    return bool(re.search(r'^\d{10}$', code))


def validate_city_code(city_code: str, city_codes: Dict[str, List[str]]) -> bool:
    """
    Validate if a city code exists in the city codes data.

    Args:
        city_code: The 3-digit city code to validate
        city_codes: Dictionary of city codes data

    Returns:
        True if the city code exists, False otherwise
    """
    return city_code in city_codes


def validate_state(state: str, city_codes: Dict[str, List[str]]) -> bool:
    """
    Validate if a state exists in the city codes data.

    Args:
        state: Name of the state in Persian
        city_codes: Dictionary of city codes data

    Returns:
        True if the state exists, False otherwise
    """
    return any(state == city_codes[city_code][0] for city_code in city_codes)


def get_city_info(city_code: str, city_codes: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Get information about a city code.

    Args:
        city_code: The 3-digit city code
        city_codes: Dictionary of city codes data

    Returns:
        Dictionary with state and city information

    Raises:
        ValueError: If the city code is not found
    """
    if not validate_city_code(city_code, city_codes):
        raise ValueError(f"City code '{city_code}' not found")

    info = city_codes[city_code]
    return {
        "state": info[0],
        "city": info[1] if len(info) > 1 else "",
        "city_code": city_code
    }


def get_available_states(city_codes: Dict[str, List[str]]) -> List[str]:
    """
    Get list of all available states.

    Args:
        city_codes: Dictionary of city codes data

    Returns:
        List of unique state names sorted alphabetically
    """
    states = set()
    for city_code in city_codes:
        states.add(city_codes[city_code][0])
    return sorted(list(states))


def get_cities_by_state(state: str, city_codes: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    """
    Get all cities for a specific state.

    Args:
        state: Name of the state in Persian
        city_codes: Dictionary of city codes data

    Returns:
        List of city information dictionaries

    Raises:
        ValueError: If the state is not found
    """
    if not validate_state(state, city_codes):
        raise ValueError(f"State '{state}' not found")

    cities = []
    for city_code in city_codes:
        if city_codes[city_code][0] == state:
            cities.append({
                "city_code": city_code,
                "city": city_codes[city_code][1] if len(city_codes[city_code]) > 1 else "",
                "state": state
            })
    return cities


def get_all_cities(city_codes: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    """
    Get all cities with their information.

    Args:
        city_codes: Dictionary of city codes data

    Returns:
        List of all city information dictionaries
    """
    cities = []
    for city_code in city_codes:
        cities.append({
            "city_code": city_code,
            "city": city_codes[city_code][1] if len(city_codes[city_code]) > 1 else "",
            "state": city_codes[city_code][0]
        })
    return cities