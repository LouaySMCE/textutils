def word_count(text):
    """
    This function takes a text (String) as input and returns the number of words in it
    """
    if text == "" or text ==" ": return 0
    count = 1
    for elm in text:
        if elm == " ":
            count+=1
    if text[-1]==" ":
        count = count -1
    return count

# Usage exemple
print(word_count("Inazuma Eleven"))
print(word_count("Hello there "))