"""Tests for char_count module."""

import pytest

from textutils.char_count import character_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 5),
        ("Hello World", 11),
        ("", 0),
        (" ", 1),
        ("   ", 3),
        ("Inazuma Eleven", 14),
    ],
)
def test_character_count(text, expected):
    """Test character_count with various strings."""
    assert character_count(text) == expected


@pytest.mark.parametrize("value", [123, None, [], True, 5.5])
def test_character_count_invalid_input(value):
    """Test that character_count raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        character_count(value)
