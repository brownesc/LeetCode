# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element 
in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""

def nextGreatestLetter(letters,target):

    #Idea, array is sorted to try and use binary Search
    #Algorithm: Use binary search to find the first element greater than targer. If target is at the end, return the first

    def firstGreaterBinarySearch(arr,target):
        start=0
        end = len(arr)-1

        
        output = -1
        while start<=end:
            mid = start+(end-start)//2
            
            if arr[mid]<=target:
                start = mid+1
            else:
                output = mid
                end = mid-1
        return (output,arr[output])
    
    index_output = firstGreaterBinarySearch(letters,target)[0]

    if index_output == -1:
        return letters[0]
    else:
        return letters[index_output]


