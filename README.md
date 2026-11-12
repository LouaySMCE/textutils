# textutils

A lightweight Python library for common text-processing operations.

## Features

- **Word counting**: Count total words with whitespace handling.
- **Character counting**: Count the number of characters in a string.
- **Text capitalization**: Capitalize string characters.
- **Text reversal**: Reverse strings.
- **Palindrome detection**: Check whether a string reads identically backwards and forwards (case-insensitive).

## Installation

Install via pip:

```bash
pip install textutils-louaysmce
```

For development:

```bash
pip install -e .[dev]
```

## Usage

```python
from textutils import (
    capitalize_words,
    character_count,
    is_palindrome,
    reverse,
    word_count,
)

# Count words
print(word_count("Hello Open Source!"))  # 3

# Count characters
print(character_count("Inazuma Eleven"))  # 14

# Capitalize text
print(capitalize_words("inazuma"))  # INAZUMA

# Reverse text
print(reverse("hello"))  # olleh

# Check palindrome
print(is_palindrome("Radar"))  # True
```

## Running Tests

Run the test suite with coverage:

```bash
pytest --cov=textutils --cov-report=term-missing
```

## Contributing

Contributions are welcome!
1. Fork the repository.
2. Create a new branch (`git switch -c feature/my-feature` or `fix/my-fix`).
3. Commit your changes with clear messages.
4. Ensure tests and pre-commit checks pass (`pre-commit run --all-files`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
