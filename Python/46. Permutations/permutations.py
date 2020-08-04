# https://leetcode.com/problems/permutations/

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def permute(nums):
    output = []
    def permuteHelper(nums,soFar=[]):
        if nums == []:
            output.append(soFar)
            return 
        for i in range(len(nums)):
            fill = soFar + [nums[i]]
            new_nums = nums[:i]+nums[i+1:]
            permuteHelper(new_nums,fill)
    permuteHelper(nums)
    return output

print(permute([1,2,3]))



        
