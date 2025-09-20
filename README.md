# Iranian National Code Generator

[![PyPI version](https://badge.fury.io/py/iranian-national-code-generator.svg)](https://pypi.org/project/iranian-national-code-generator/)
[![Python Versions](https://img.shields.io/pypi/pyversions/iranian-national-code-generator.svg)](https://pypi.org/project/iranian-national-code-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/benyaminsalimi/Iranian-national-code-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/benyaminsalimi/Iranian-national-code-generator/actions)

A Python library for generating and validating Iranian national codes (social security numbers).

## Installation

Install from PyPI:

```bash
pip install iranian-national-code-generator
```

Or install from source:

```bash
git clone https://github.com/benyaminsalimi/Iranian-national-code-generator.git
cd Iranian-national-code-generator
pip install -e .
```

## Usage

### Basic Usage

```python
from iranian_national_code_generator import IranianNationalCodeGenerator

# Create an instance
generator = IranianNationalCodeGenerator()

# Validate a national code
is_valid = generator.validate("0123456789")
print(f"Is valid: {is_valid}")  # True

# Generate codes for a specific state (memory-efficient generator)
tehran_codes = generator.generate_by_state("تهران")
print("First 5 Tehran codes:")
for i, code in enumerate(tehran_codes):
    if i >= 5:
        break
    print(f"  {code}")

# Generate codes for a specific city
city_codes = generator.generate_by_city_code("001")
print("First 3 codes for city 001:")
for i, code in enumerate(city_codes):
    if i >= 3:
        break
    print(f"  {code}")

# Convert generator to list if needed (be careful with memory usage)
all_tehran_codes = list(generator.generate_by_state("تهران"))
print(f"Total Tehran codes: {len(all_tehran_codes)}")

# Generate all possible valid Iranian national codes
all_codes = generator.generate_all()
print("First 10 valid codes:")
for i, code in enumerate(all_codes):
    if i >= 10:
        break
    print(f"  {code}")

# Get information about a city code
city_info = generator.get_city_info("001")
print(f"City info: {city_info}")

# Get all available states
states = generator.get_available_states()
print(f"Available states: {states[:5]}")  # First 5 states
```

### Direct Validation

```python
from iranian_national_code_generator import validate_national_code, is_valid_format

# Validate a code directly
is_valid = validate_national_code("0123456789")
print(f"Is valid: {is_valid}")

# Check format only
is_correct_format = is_valid_format("0123456789")
print(f"Correct format: {is_correct_format}")
```

### City and State Validation

```python
from iranian_national_code_generator import (
    validate_city_code,
    validate_state,
    get_city_info,
    get_available_states,
    get_cities_by_state,
    get_all_cities
)

# Create generator instance to access city_codes data
generator = IranianNationalCodeGenerator()

# Validate city code
is_valid_city = validate_city_code("001", generator.city_codes)
print(f"Is valid city code: {is_valid_city}")

# Validate state
is_valid_state = validate_state("تهران", generator.city_codes)
print(f"Is valid state: {is_valid_state}")

# Get city information
city_info = get_city_info("001", generator.city_codes)
print(f"City info: {city_info}")

# Get all available states
states = get_available_states(generator.city_codes)
print(f"Available states: {states[:3]}")

# Get cities by state
tehran_cities = get_cities_by_state("تهران", generator.city_codes)
print(f"Tehran cities: {len(tehran_cities)}")

# Get all cities
all_cities = get_all_cities(generator.city_codes)
print(f"Total cities: {len(all_cities)}")
```

### Command Line Usage

You can also use the library from the command line (requires installing the package):

```bash
# Validate a specific code
python -c "from iranian_national_code_generator import validate_national_code; print(validate_national_code('0123456789'))"

# Get available states
python -c "from iranian_national_code_generator import IranianNationalCodeGenerator; g = IranianNationalCodeGenerator(); print(g.get_available_states()[:3])"

# Validate city code
python -c "from iranian_national_code_generator import IranianNationalCodeGenerator, validate_city_code; g = IranianNationalCodeGenerator(); print(validate_city_code('001', g.city_codes))"

# Get city information
python -c "from iranian_national_code_generator import IranianNationalCodeGenerator, get_city_info; g = IranianNationalCodeGenerator(); print(get_city_info('001', g.city_codes))"

# Generate first 5 codes for Tehran (using generator)
python -c "from iranian_national_code_generator import IranianNationalCodeGenerator; g = IranianNationalCodeGenerator(); codes = g.generate_by_state('تهران'); print([next(codes) for _ in range(5)])"
```

## Installation

Install from PyPI:

```bash
pip install ir-national-code
```

Or install from source:

```bash
git clone https://github.com/benyaminsalimi/Iranian-national-code-generator.git
cd Iranian-national-code-generator
pip install -e .
```

## Usage

### Basic Usage

```python
from ir_national_code import ir_national_code

# Create an instance
generator = ir_national_code()

# Validate a national code
is_valid = generator.validate("0123456789")
print(f"Is valid: {is_valid}")  # True

# Generate all valid codes for a specific state
tehran_codes = generator.generate_by_state("تهران")
print(f"Number of Tehran codes: {len(tehran_codes)}")

# Generate all valid codes for a specific city code
city_codes = generator.generate_by_city_code("001")
print(f"Number of codes for city 001: {len(city_codes)}")

# Generate all possible valid Iranian national codes
all_codes = generator.generate_all()
print(f"Total valid codes: {len(all_codes)}")
```

### Command Line Usage

You can also use the library from the command line (requires installing the package):

```bash
# Generate codes for a specific state
python -c "from iranian_national_code_generator import IranianNationalCodeGenerator; g = IranianNationalCodeGenerator(); codes = g.generate_by_state('تهران'); print(f'Generated {len(codes)} codes')"

# Validate a specific code
python -c "from iranian_national_code_generator import validate_national_code; print(validate_national_code('0123456789'))"
```

## API Reference

### `IranianNationalCodeGenerator()`

Main class for Iranian national code operations.

#### Methods

- `validate(code: str) -> bool`: Validates if a given 10-digit code is a valid Iranian national code
- `generate_all() -> List[str]`: Returns all possible valid Iranian national codes
- `generate_by_state(state_name: str) -> List[str]`: Returns all valid national codes for a given state
- `generate_by_city_code(city_code: str) -> List[str]`: Returns all valid national codes for a given city code
- `get_city_info(city_code: str) -> Dict[str, Any]`: Returns information about a city code
- `get_available_states() -> List[str]`: Returns list of all available states
- `get_cities_by_state(state: str) -> List[Dict[str, Any]]`: Returns all cities for a specific state

### Standalone Functions

- `validate_national_code(code: str) -> bool`: Validates an Iranian national code
- `is_valid_format(code: str) -> bool`: Checks if the code has the correct format (10 digits)

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/benyaminsalimi/Iranian-national-code-generator.git
cd Iranian-national-code-generator

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=ir_national_code

# Run specific test file
pytest tests/test_ir_national_code.py
```

### Code Quality

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pre-commit**: Git hooks for automated quality checks

Run all quality checks:

```bash
pre-commit run --all-files
```

### Building and Publishing

```bash
# Build the package
python -m build

# Upload to PyPI (requires API token)
twine upload dist/*
```

## Data Source

The city codes data is sourced from [fandogh/codemeli](https://github.com/fandogh/codemeli/docs).

## Validation Algorithm

The validation algorithm is based on the Iranian national code checksum calculation from [this gist](https://gist.github.com/ebraminio/5292017).

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Run pre-commit hooks
7. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Thanks to [fandogh](https://github.com/fandogh/codemeli/docs) for the city codes data
- Thanks to [ebraminio](https://gist.github.com/ebraminio/5292017) for the validation algorithm