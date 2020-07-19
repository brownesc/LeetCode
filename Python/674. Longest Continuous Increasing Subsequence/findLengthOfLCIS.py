# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
"""
def findLengthOfLCIS(nums):
    max_length = 0
    total_length = 0
    start = -float("INF")
    for i in range(len(nums)):
        num = nums[i]
        if num>start:
            start = num
            total_length+=1
        elif num<=start:
            max_length= max(max_length,total_length)
            total_length=0
        if i==len(nums)-1:
            max_length= max(max_length,total_length)
            total_length=0
        print(total_length)
    return max_length

print(findLengthOfLCIS([1,3,5,7]))
