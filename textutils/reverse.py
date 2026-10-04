def reverse(text):
    """
    This function takes a text (string) as input and makes it backwards.
    """
    L=[]
    for elm in text:
        L.append(elm)
    N = L[::-1]
    new_text = ""
    for elm in N:
        new_text = new_text + elm
    return new_text

# Usage exemple
print(reverse("hello there"))