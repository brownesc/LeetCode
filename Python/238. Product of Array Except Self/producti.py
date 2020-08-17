# https://leetcode.com/problems/product-of-array-except-self/

"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the 
elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) 
fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space 
complexity analysis.)
"""
def productExceptSelf(nums):
    left_product = []
    right_product = []
    product = 1
    for num in nums:
        product*=num
        left_product.append(product)
    #Reset for right side
    product = 1        
    for i in range(len(nums)-1,-1,-1):
        product*=nums[i]
        right_product.append(product)
    #fix the reversal    
    right_product = right_product[::-1]

    for i in range(len(nums)):
        if i==0:
            nums[i]=right_product[i+1]
        elif i==len(nums)-1:
            nums[i]=left_product[i-1]
        else:
            nums[i]= left_product[i-1]*right_product[i+1]

    return nums

print(productExceptSelf([1,2,3]))
        
    
