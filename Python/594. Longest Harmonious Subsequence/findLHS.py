# https://leetcode.com/problems/longest-harmonious-subsequence/

"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""
#Can do O(n**2)
def findLHS(nums):
    # max_output_length = 0
    # output = []
    # for i in range(len(nums)):
    #     maximum = nums[i]
    #     inter = []
    #     inter_length = 0
    #     for j in range(len(nums)):
    #         if maximum-nums[j]>=0 and maximum-nums[j]<=1:
    #             inter.append(nums[j])
    #             inter_length+=1
    #     if inter_length>max_output_length:
    #         max_output_length = inter_length
    # return max_output_length 
    counter = {}
    minus_one = {}
    for num in nums:
        counter[num] = counter.get(num,0)+1
        minus_one[num+1] = minus_one.get(num+1,0)+1
    
    max_length = 0
    for num in counter:
        
        if minus_one.get(num,0)!=0:
            temp_lenght = counter[num]+ minus_one[num]
            if temp_lenght>max_length:
                max_length=temp_lenght
    return max_length
        

print(findLHS([1,1,1,1]))
print(findLHS([1,3,2,2,5,2,3,7]))
