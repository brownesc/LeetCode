# https://leetcode.com/problems/top-k-frequent-elements/

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

def topKFrequent(nums,k):
    # counter = {}

    # for digit in nums:
    #     counter[digit]=counter.setdefault(digit,0)+1
    
    # min_set = set()
    # for digit in nums:
    #     min_set.add(digit)
    #     if len(min_set)>k:
    #         min_set.remove(min(min_set,key=lambda x:counter[x]))
    # return list(min_set)
    pass

def hoare_partition(arr,low,high):
    pivot = arr[low]
    i = low-1
    j = high+1

    while True:
        #Find leftmost element greater than or equal to pivot
        i+=1
        while arr[i]<pivot:
            i+=1
        #Find right most smaller than or equal to pivot
        j-=1
        while arr[j]>pivot:
            j-=1
        if i >= j: #if pointers meet
            print(arr)
            return j
        #swap
        arr[i],arr[j] = arr[j],arr[i]

print(hoare_partition([3,1,2,4,7],0,2))
# print(topKFrequent([1,1,1,2,2,3],2))