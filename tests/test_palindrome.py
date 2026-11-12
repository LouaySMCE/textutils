"""Tests for palindrome module."""

import pytest

from textutils.palindrome import is_palindrome


@pytest.mark.parametrize(
    "value, expected",
    [
        ("radar", True),
        ("hello", False),
        ("Radar", True),
        ("", True),
        ("a", True),
        ("ab", False),
        ("Racecar", True),
        ("rad ar", False),
    ],
)
def test_is_palindrome(value, expected):
    """Test palindrome detection with valid string inputs."""
    assert is_palindrome(value) == expected


@pytest.mark.parametrize("value", [123, None, [], True])
def test_is_palindrome_rejects_non_strings(value):
    """Test that is_palindrome raises TypeError on non-string inputs."""
    with pytest.raises(TypeError):
        is_palindrome(value)
