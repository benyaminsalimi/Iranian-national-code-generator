"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture(scope="session")
def sample_valid_codes():
    """Sample valid Iranian national codes for testing."""
    return [
        "0491570006",
        "0123456789",
        "1111111111",
    ]


@pytest.fixture(scope="session")
def sample_invalid_codes():
    """Sample invalid codes for testing."""
    return [
        "123456789",    # Too short
        "12345678901",  # Too long
        "123456789a",   # Contains letter
        "123456789 ",   # Contains space
        "",             # Empty string
    ]