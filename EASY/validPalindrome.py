# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


def validPalindrome(s):
    filtered = filter(lambda cha: cha.isalnum(), s)
    lower_case = map(lambda cha: cha.lower(), filtered)
    list_strings = list(lower_case)
    reversed_str = list_strings[::-1]
    return list_strings == reversed_str

#tests
#test1
s = "A man, a plan, a canal: Panama"
ans = validPalindrome(s)
print(ans)

#test2
s2 ="race a car"
ans2 = validPalindrome(s2)
print(ans2)

#test3
s3 = " "
ans3 = validPalindrome(s3)
print(ans3)