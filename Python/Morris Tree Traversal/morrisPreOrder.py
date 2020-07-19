"""
Using Morris Traversal, we can traverse the tree without using stack and recursion. The algorithm for Preorder is almost similar to Morris traversal for Inorder.
1...If left child is null, print the current node data. Move to right child.
….Else, Make the right child of the inorder predecessor point to the current node. Two cases arise:
………a) The right child of the inorder predecessor already points to the current node. Set right child to NULL. Move to right child of current node.
………b) The right child is NULL. Set it to current node. Print current node’s data and move to left child of current node.
2...Iterate until current node is not NULL.

Following is the implementation of the above algorithm.
"""

# Python program for Morris Preorder traversal 
  
# A binary tree Node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Preorder traversal without  
# recursion and without stack 
def MorrisTraversal(root): 
    curr = root 
  
    while curr: 
        # If left child is null, print the 
        # current node data. And, update  
        # the current pointer to right child. 
        if curr.left is None: 
            print(curr.data, end= " ") 
            curr = curr.right 
  
        else: 
            # Find the inorder predecessor 
            prev = curr.left 
  
            while prev.right is not None and prev.right is not curr: 
                prev = prev.right 
  
            # If the right child of inorder 
            # predecessor already points to 
            # the current node, update the  
            # current with it's right child 
            if prev.right is curr: 
                prev.right = None
                curr = curr.right 
                  
            # else If right child doesn't point 
            # to the current node, then print this 
            # node's data and update the right child 
            # pointer with the current node and update 
            # the current with it's left child 
            else: 
                print (curr.data, end=" ") 
                prev.right = curr  
                curr = curr.left 
  
# Function for sStandard preorder traversal 
def preorfer(root): 
    if root : 
        print(root.data, end = " ") 
        preorfer(root.left) 
        preorfer(root.right) 
          
  
# Driver program to test  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
  
root.left.left = Node(4) 
root.left.right = Node(5) 
  
root.right.left= Node(6) 
root.right.right = Node(7) 
  
root.left.left.left = Node(8) 
root.left.left.right = Node(9) 
  
root.left.right.left = Node(10) 
root.left.right.right = Node(11) 
  
  
MorrisTraversal(root) 
print("\n") 
preorfer(root) 
  
  
# This code is contributed by 'Aartee'