"""Palindrome detection module."""


def is_palindrome(s):
    """Check if the given string is a palindrome, ignoring case.

    Parameters
    ----------
    s : str
        Input string to check.

    Returns
    -------
    bool
        True if the string is a palindrome, False otherwise.

    Raises
    ------
    TypeError
        If s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
