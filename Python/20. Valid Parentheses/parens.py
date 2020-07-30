# https://leetcode.com/problems/valid-parentheses/
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
def isValid(s):
    right_to_left = {"}":"{","]":"[",")":"("}
    left_stack = []

    for brack in s:
        if brack in right_to_left:
            last_seen = left_stack.pop()
            if last_seen != right_to_left[brack]:
                return False
        else:
            left_stack.append(brack)
    return True

print(isValid("([)]"))