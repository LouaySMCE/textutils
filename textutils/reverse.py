"""Text reverse module."""


def reverse(text):
    """Reverse a string.

    Parameters
    ----------
    text : str
        Input text to reverse.

    Returns
    -------
    str
        Reversed text.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]
