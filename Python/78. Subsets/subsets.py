# https://leetcode.com/problems/subsets/

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def subsets(nums):
    output = []
    def helper(soFar=[],n=0):
        if n == len(nums):
            output.append(soFar)
        
        else:
            helper(soFar+[nums[n]],n+1)
            helper(soFar,n+1)
    helper()
    return output

print(subsets([1,2,3]))