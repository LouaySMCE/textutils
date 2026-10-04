"""
Check if a string is a palindrome.
A palindrome is a word that is the same forward and backward.
"radar" -> True , "level" -> False
"""

def is_palindrome(s):
    """
    returns true if the given string is a palindrome
    """
    L = []
    for i in range(len(s)):
        if s[i] == s[-1-i]:
            L.append(True)
        else:
            L.append(False)
    if False in L:
        return False
    else:
        return True

print(is_palindrome("radar"))
print(is_palindrome("hello"))