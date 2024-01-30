# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
from collections import Counter
def ramsome(s, t):
    store_s = Counter(s)
    for i in range(len(t)):
        if t[i] in store_s:
            store_s[t[i]] -= 1
            if store_s[t[i]] == 0:
                del store_s[t[i]]
        else:
            return False
    return True
