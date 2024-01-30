# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
from collections import Counter

def validAnagram(s, t):
    return Counter(s) == Counter(t)


#test
#test1
s1 = "anagram" 
t1 = "ramanag"
ans = validAnagram(s1, t1)
print(ans)