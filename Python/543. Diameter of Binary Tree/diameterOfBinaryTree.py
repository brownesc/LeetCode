"""
Intuition

Any path can be written as two arrows (in different directions) from some node, where an arrow is a path that starts at some node 
and only travels down to child nodes.

If we knew the maximum length arrows L, R for each child, then the best path touches L + R + 1 nodes.

Algorithm

Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1. While we do, a path "through" this node uses 
1 + (depth of node.left) + (depth of node.right) nodes. Let's search each node and remember the highest number of nodes used in some path. The desired 
length is 1 minus this number.
"""
class Solution:
    def diameterOfBinaryTree(self,root):
        longest = 1
        def maxDepth(root):
            nonlocal longest
            if root:
                L= maxDepth(root.left)
                R = maxDepth(root.right)
                longest = max(longest,L+R+1)
                return 1+max(L,R)
            else:
                return 0
        maxDepth(root)
        return longest-1