# https://leetcode.com/problems/subtree-of-another-tree/
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(s,t):
    def printPreorderTree(root,isLeft):
        if root:
            return "#"+str(root.val)+ " " + printPreorderTree(root.left,True) + printPreorderTree(root.right,False)

        else:
            if isLeft:
                return #LNull
            else:
                return #RNull
    stringified_s = printPreorderTree(s,True)
    stringified_t = printPreorderTree(t,True)

    def KMP(pattern, text):
        output_indices = []
        pattern_length = len(pattern)
        text_length = len(text)
        longest_prefix_suffix_array = [0]*pattern_length
        pattern_index = 0
        text_index = 0
        lps_construction(pattern,pattern_length,longest_prefix_suffix_array)

        while text_index < text_length:
            if text[text_index] == pattern[pattern_index]:
                #Char matches, move forward
                pattern_index += 1
                text_index += 1
            
            #We've reached a patterns
            if pattern_index == pattern_length:
                print("Found at index"+ str(text_index-pattern_index))
                output_indices.append(text_index-pattern_index)
                pattern_index = longest_prefix_suffix_array[pattern_index-1]
            
            elif text_index < text_length and pattern[pattern_index] != text[text_index]:
                #First mismatch, but we don't have to go back to the beging
                if pattern_index !=0:
                    pattern_index = longest_prefix_suffix_array[pattern_index-1]
                #No possible matches, have to start over
                else:
                    text_index+=1
        
        return output_indices
    def lps_construction(pattern, pattern_length, longest_prefix_suffix_array):
        maximum_previous_prefix_suffix_length = 0
        i = 1 

        while i < pattern_length:
            if pattern[maximum_previous_prefix_suffix_length] == pattern[i]:
                maximum_previous_prefix_suffix_length+=1
                longest_prefix_suffix_array[i]= maximum_previous_prefix_suffix_length
                i+=1
            else:
                if maximum_previous_prefix_suffix_length != 0 :
                    maximum_previous_prefix_suffix_length = longest_prefix_suffix_array[maximum_previous_prefix_suffix_length-1]
                
                else:
                    longest_prefix_suffix_array[i] = 0
                    i += 1

    final_output = KMP(stringified_t, stringified_s)

    if final_output:
        return True
    else:
        return False
