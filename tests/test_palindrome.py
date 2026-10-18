import pytest

from palindrome import is_palindrome


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
    assert is_palindrome(value) == expected


@pytest.mark.parametrize("value", [123, None, [], True])
def test_is_palindrome_rejects_non_strings(value):
    with pytest.raises(TypeError):
        is_palindrome(value)