"""
Check if a string is a palindrome.
"""


def is_palindrome(s):
    """Return True if the string is a palindrome, ignoring case."""

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(is_palindrome("radar"))
print(is_palindrome("hello"))