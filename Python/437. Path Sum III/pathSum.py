# https://leetcode.com/problems/path-sum-iii/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
from collections import defaultdict
def pathSum(root,target):
    # Initialize all counts to 0
    prev = defaultdict(lambda: 0)
    ans = 0
    
    def DFS(root,rs):
        nonlocal ans
        if root:
            rs+=root.val
            
            #The total is found, so advance
            if rs==target:
                ans+=1
            # currsum exceeds given sum by currsum  - sum. 
            # Find number of subarrays having   
            # this sum and exclude those subarrays  
            # from currsum by increasing count by   
            # same amount.
            if rs-target in prev:
                ans+=prev[rs-target]
                
            prev[rs]+=1
            if root.left:
                DFS(root.left,rs)
            if root.right:
                DFS(root.right,rs)
            # Add currsum value to count of   
            # different values of sum. 
            prev[rs]-=1
        
        else:
            return 0
    DFS(root,0)
    return ans