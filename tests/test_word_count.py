"""Tests for word_count module."""

import pytest

from textutils.word_count import word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 1),
        ("Hello World", 2),
        ("", 0),
        ("   ", 0),
        (" Hello World ", 2),
        ("Hello   World", 2),
        ("One two three four five", 5),
    ],
)
def test_word_count(text, expected):
    """Test word_count with normal and edge cases."""
    assert word_count(text) == expected


@pytest.mark.parametrize("value", [123, None, [], True, 3.14])
def test_word_count_invalid_input(value):
    """Test that word_count raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        word_count(value)
