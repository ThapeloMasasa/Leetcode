# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def validParentheses(s):
    store = {")":"(", "]":"[", "}":"{"}
    stack = []
    for bracket in s:
        if bracket in store.keys() and not stack:
            return False
        elif bracket in store.values():
            stack.append(bracket)
        elif bracket in store.keys() and stack:
            top = stack.pop()
            if top != store[bracket]:
                return False
    return not stack

#tests
#test1
s1 = "()"
print(validParentheses(s1))
#test2
s2 = "()[]{}"
print(validParentheses(s2))
#test3
s3 = "(]"
print(validParentheses(s3))