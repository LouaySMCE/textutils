"""Word count module."""


def word_count(text):
    """Count the number of words in a string.

    Parameters
    ----------
    text : str
        Input text whose words are counted.

    Returns
    -------
    int
        Number of words in the input text.

    Raises
    ------
    TypeError
        If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())
