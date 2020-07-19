# https://leetcode.com/problems/maximum-subarray/
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

def maxSubArrayOOfN(nums):
    max_so_far = 0
    intermdiate_total = 0
    for i in range(len(nums)):
        intermdiate_total += nums[i]
        max_so_far = max(max_so_far, intermdiate_total)
        if intermdiate_total<0:
            intermdiate_total = 0
    
    return max_so_far

"""
Approach 1: Divide and Conquer
Intuition

The problem is a classical example of divide and conquer approach, and can be solved with the algorithm similar with the merge sort.

Let's follow here a solution template for the divide and conquer problems :

Define the base case(s).

Split the problem into subproblems and solve them recursively.

Merge the solutions for the subproblems to obtain the solution for the original problem.

Algorithm

maxSubArray for array with n numbers:

If n == 1 : return this single element.

left_sum = maxSubArray for the left subarray, i.e. for the first n/2 numbers (middle element at index (left + right) / 2 always belongs to the left subarray).

right_sum = maxSubArray for the right subarray, i.e. for the last n/2 numbers.

cross_sum = maximum sum of the subarray containing elements from both left and right subarrays and hence crossing the middle element at index (left + right) / 2.

Merge the subproblems solutions, i.e. return max(left_sum, right_sum, cross_sum).
"""

class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)
    
    