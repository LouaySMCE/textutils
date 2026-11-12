"""Character count module."""


def character_count(text):
    """Count the number of characters in a string.

    Parameters
    ----------
    text : str
        Input text whose characters are counted.

    Returns
    -------
    int
        Number of characters in the input text.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text)
