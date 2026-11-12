"""A lightweight Python library for common text-processing operations."""

from textutils.capitalize import capitalize_words
from textutils.char_count import character_count
from textutils.palindrome import is_palindrome
from textutils.reverse import reverse
from textutils.word_count import word_count

__all__ = [
    "capitalize_words",
    "character_count",
    "is_palindrome",
    "reverse",
    "word_count",
]
