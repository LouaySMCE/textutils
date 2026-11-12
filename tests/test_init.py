"""Tests for top-level package exports."""

import textutils


def test_package_exports():
    """Verify that textutils exports all expected public functions."""
    assert hasattr(textutils, "word_count")
    assert hasattr(textutils, "character_count")
    assert hasattr(textutils, "reverse")
    assert hasattr(textutils, "capitalize_words")
    assert hasattr(textutils, "is_palindrome")
