# https://leetcode.com/problems/find-pivot-index/

"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
 
Constraints:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""

def pivotIndex(nums):
    #Create a table of sums. If total_sum - sum_up_to(i) == sum_up_to(i-1)
    total = sum(nums)
    sum_up_to = []
    output = -1
    #Process the sum array
    for i in range(len(nums)):
        if i:
            sum_up_to.append(nums[i]+sum_up_to[i-1])
        else:
            sum_up_to.append(nums[i])
    
    for i in range(1,len(nums)-1):
        if sum_up_to[i-1]==sum_up_to[len(nums)-1]-sum_up_to[i]:
            return i
    return output


def pivotIndex1(nums):
    #Create a table of sums. If total_sum - sum_up_to(i) == sum_up_to(i-1)
    total = sum(nums)
    prefix_sum = []
    output = -1
    #Process the sum array
    for i in range(len(nums)):
        if i:
            prefix_sum.append(nums[i-1]+prefix_sum[i-1])
        else:
            prefix_sum.append(0)
    
    for i in range(len(nums)):
        if i == len(nums)-1:
            if prefix_sum[i]==0:
                return i 
        elif prefix_sum[i]==total-prefix_sum[i+1]:
            return i
    return output