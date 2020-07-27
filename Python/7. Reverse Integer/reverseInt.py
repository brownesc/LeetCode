# https://leetcode.com/problems/reverse-integer/

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def reverse(x):
    min_int = -2**31
    max_int = (2**31)-1

    output = 0 
    num = x
    is_Negative = False
    if num<0:
        num = -num
        is_Negative = True
    while num!= 0:
        num, remainder = divmod(num, 10)
        
        output*=10
        output+=remainder
    if output<min_int or output> max_int:
        return 0
    elif is_Negative:
        return -output
    else:
        return output
print(reverse(-1002))