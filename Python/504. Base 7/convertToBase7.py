# https://leetcode.com/problems/base-7/

"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"

"""

def convertToBase7(num):
    output_string = ""
    num_to_process = num

    while True:
        quotient, remainder = divmod(num_to_process,7)
        output_string+=str(remainder)
        num_to_process = quotient
        if num_to_process ==0:
            break

    return output_string[::-1]

print(convertToBase7(700))
print(convertToBase7(13))