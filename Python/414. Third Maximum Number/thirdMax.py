# https://leetcode.com/problems/third-maximum-number/

"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

def thirdMax(nums):
    if len(nums)<3:
        return max(nums)
    
    else:
        first_max = None
        second_max = None
        third_max = None

        for digit in nums:
            if first_max is None:
                print("first")
                first_max = digit
            elif second_max is None:
                print('sec')
                if digit<first_max:
                    second_max = digit
                else:
                    second_max = first_max
                    first_max = digit
            elif third_max is None:
                print("I made it")
                if digit>first_max:
                    third_max = second_max 
                    second_max = first_max
                    first_max = digit
                
                elif digit>second_max:
                    third_max = second_max
                    digit = second_max
                
                else:
                    third_max = digit
            else:
                if digit>first_max:
                    third_max = second_max
                    second_max = first_max
                    first_max = digit
                
                elif digit>second_max:
                    third_max = second_max
                    second_max = digit
                
                elif digit > third_max:
                    third_max = digit
            print((first_max,second_max,third_max))
        return third_max

print(thirdMax([2,2,3,1]))