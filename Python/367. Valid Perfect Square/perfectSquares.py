# https://leetcode.com/problems/valid-perfect-square/
"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
"""


def isPerfectSquare(num):
    start = 1
    end = num
    while start<=end:
        mid = start + (end-start)//2
        mid_squared = mid**2

        if mid_squared == num:
            return True
        elif mid_squared < num:
            start = mid+1
        else:
            end = mid-1 
    return False
print()