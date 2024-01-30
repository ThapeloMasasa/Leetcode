# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
from collections import Counter
def longestPalindrome(s):
    store_s = Counter(s)
    ans = []
    odd = 0

    for times in store_s.values():
        ans.append(times)
        if times%2 != 0:
            odd += 1

    if odd == 0:
        return sum(ans) - odd
    else:
        return sum(ans) - odd + 1
