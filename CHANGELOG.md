# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-11-12

### Added
- Core text processing functions in `textutils`:
  - `word_count`: Counts number of words in a string.
  - `character_count`: Counts number of characters in a string.
  - `capitalize_words`: Capitalizes characters in a string.
  - `reverse`: Reverses the string characters.
  - `is_palindrome`: Case-insensitive palindrome detection.
- Type validation raising `TypeError` for non-string inputs.
- NumPy-style docstrings for all modules and public functions.
- Unit test suite with `pytest` covering normal, edge, and exception cases.
- Test coverage configuration with `pytest-cov`.
- Local automation with `pre-commit` running `black` and `ruff`.
- GitHub Actions CI workflow testing on Ubuntu and macOS across Python 3.11 and 3.12.
- GitHub Actions release workflow for publishing to PyPI.
