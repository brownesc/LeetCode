import deque from collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Approach 1: Recursion: DFS Preorder Traversal
Intuition

The first step is to ensure that the tree is not empty. The second step is to implement the recursive function helper(node, level), which takes the current 
node and its level as the arguments.

Algorithm for the Recursive Function

Here is its implementation:

Initialize the output list levels. The length of this list determines which level is currently updated. You should compare this level len(levels) with a 
node level level, to ensure that you add the node on the correct level. If you're still on the previous level - add the new level by adding a new list into levels.

Append the node value to the last level in levels.

Process recursively child nodes if they are not None: helper(node.left / node.right, level + 1).
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels[::-1]
"""
Approach 2: Iteration: BFS Traversal
Algorithm

The recursion above could be rewritten in the iteration form.

Let's keep each tree level in the queue structure, which typically orders elements in a FIFO (first-in-first-out) manner. 
In Java one could use ArrayDeque implementation of the Queue interface. In Python using Queue structure would be an overkill 
since it's designed for a safe exchange between multiple threads and hence requires locking which leads to a performance downgrade. 
In Python the queue implementation with a fast atomic append() and popleft() is deque.

Algorithm

Initialize two queues: one for the current level, and one for the next. Add root into nextLevel queue.

While nextLevel queue is not empty:

Initialize the current level currLevel = nextLevel, and empty the next level nextLevel.

Iterate over the current level queue:

Append the node value to the last level in levels.

Add first left and then right child node into nextLevel queue.

Return reversed levels.
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        next_level = deque([root])
        
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])
            
            for node in curr_level:
                # append the current node value
                levels[-1].append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
        return levels[::-1]
