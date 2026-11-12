"""Tests for capitalize module."""

import pytest

from textutils.capitalize import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "HELLO"),
        ("inazuma", "INAZUMA"),
        ("Hello World", "HELLO WORLD"),
        ("", ""),
        ("123 abc", "123 ABC"),
    ],
)
def test_capitalize_words(text, expected):
    """Test capitalize_words with strings."""
    assert capitalize_words(text) == expected


@pytest.mark.parametrize("value", [123, None, [], True])
def test_capitalize_words_invalid_input(value):
    """Test that capitalize_words raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        capitalize_words(value)
