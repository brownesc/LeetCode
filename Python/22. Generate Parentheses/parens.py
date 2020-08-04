# https://leetcode.com/problems/generate-parentheses/
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""



def generateParenthesis(n):
    output = []
    def helper(S='',left=0,right=0):
        if len(S)==2*n:
            output.append(S)
        if left<n:
            helper(S+'(',left+1,right)
        if right<left:
            helper(S+')',left,right+1)
    helper()
    return output
print(generateParenthesis(4))