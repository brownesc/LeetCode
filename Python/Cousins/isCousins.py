# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Algorithm

Start traversing the tree from the root node. Look for Node x and Node y.

Record the depth when the first node i.e. either of x or y is found and return true.

Once one of the nodes is discovered, for every other recursive call after this discovery, we return false if the current 
depth is more than the recorded depth. This basically means we didn't find the other node at the same depth and there is 
no point going beyond. This step of pruning helps to speed up the recursion by reducing the number of recursive calls.

Return true when the other node is discovered and has the same depth as the recorded depth.

Recurse the left and the right subtree of the current node. If both left and right recursions return true and the current 
node is not their immediate parent, then Node x and Node y are cousins. Thus, isCousin is set to value true.
"""
class Solution:

    def __init__(self):
        # To save the depth of the first node.
        self.recorded_depth = None
        self.is_cousin = False

    def dfs(self, node, depth, x, y):
        if node is None:
            return False

        # Don't go beyond the depth restricted by the first node found.
        if self.recorded_depth and depth > self.recorded_depth:
            return False

        if node.val == x or node.val == y:
            if self.recorded_depth is None:
                # Save depth for the first node.
                self.recorded_depth = depth
            # Return true, if the second node is found at the same depth.
            return self.recorded_depth == depth

        left = self.dfs(node.left, depth+1, x, y)
        right = self.dfs(node.right, depth+1, x, y)

        # self.recorded_depth != depth + 1 would ensure node x and y are not
        # immediate child nodes, otherwise they would become siblings.
        if left and right and self.recorded_depth != depth + 1:
            self.is_cousin = True

        return left or right

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # Recurse the tree to find x and y
        self.dfs(root, 0, x, y)
        return self.is_cousin

"""
BFS With Early Stopping

Algorithm

Do a level order traversal of the tree using a queue.

For every node that is popped off the queue, check if the node is either Node x or Node y. If it is, then for the first time, set both 
siblings and cousins flags as true. The flags are set as true to mark the possibility of siblings or cousins.

To distinguish siblings from cousins, we insert markers in the queue. After inserting the children for each node, we also insert a null 
marker. This marker defines a boundary for each set of siblings and hence helps us to differentiate a pair of siblings from cousins.

Whenever we encounter the null marker during our traversal, we set the siblings flag to false. This is because the marker marks the
 end of the siblings territory.

The second time we encounter a node which is equal to Node x or Node y we will have clarity about whether or not we are still within the 
siblings boundary. If we are within the siblings boundary, i.e. if the siblings flag is still true, then we return false. Otherwise, we return true.
"""
from collections import defaultdict
class Solution2:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        # Queue for BFS
        queue = collections.deque([root])

        while queue:

            siblings = False
            cousins = False
            nodes_at_depth = len(queue)
            for _ in range(nodes_at_depth):

                # FIFO
                node = queue.popleft()     

                # Encountered the marker.
                # Siblings should be set to false as we are crossing the boundary.
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        # Set both the siblings and cousins flag to true
                        # for a potential first sibling/cousin found.
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            # If the siblings flag is still true this means we are still
                            # within the siblings boundary and hence the nodes are not cousins.
                            return not siblings

                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    # Adding the null marker for the siblings
                    queue.append(None)
            # After the end of a level if `cousins` is set to true
            # This means we found only one node at this level
            if cousins:
                return False

        return False