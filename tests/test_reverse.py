"""Tests for reverse module."""

import pytest

from textutils.reverse import reverse


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "olleh"),
        ("hello there", "ereht olleh"),
        ("", ""),
        ("a", "a"),
        ("racecar", "racecar"),
        ("12345", "54321"),
    ],
)
def test_reverse(text, expected):
    """Test reverse with normal and edge cases."""
    assert reverse(text) == expected


@pytest.mark.parametrize("value", [123, None, [], True, [1, 2]])
def test_reverse_invalid_input(value):
    """Test that reverse raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        reverse(value)
