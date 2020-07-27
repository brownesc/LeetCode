# https://leetcode.com/problems/non-decreasing-array/
"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""


def checkPossibility(nums):
    count = 0 
    for index in range(len(nums)):
        if index:
            if nums[index-1]<=nums[index]:
                continue
            else:
                count+=1
        else:
            continue
    
    return count==1 or count ==2 or not count

        
print(checkPossibility([-1]))
