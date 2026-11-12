"""Capitalization module."""


def capitalize_words(text):
    """Capitalize all letters in a string.

    Parameters
    ----------
    text : str
        Input text to capitalize.

    Returns
    -------
    str
        Capitalized text.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.upper()
