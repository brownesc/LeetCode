# https://leetcode.com/problems/merge-sorted-array/
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""

    


def merge(nums1,m,nums2,n):
    #try starting from the back
    i=m-1 #back of first array
    j = n-1 #back of second array
    k=m+n-1 #back of array ith lst 0s

    while i>=0 and j>=0:
        if nums1[i]>=nums2[j]:
            nums1[k] = nums1[i]
            i-=1
            k-=1

        else:
            nums1[k] = nums2[j]
            j-=1
            k-=1
    nums1[:j + 1] = nums2[:j + 1]

    return (nums1,nums2,i,j,k)

print(merge([1,5,7,0,0,0],3,[3,4,6],3))
print(merge([4,5,6,0,0,0],3,[1,2,3],3))
print(merge([1,2,3,0,0,0],3,[4,5,6],3))

            