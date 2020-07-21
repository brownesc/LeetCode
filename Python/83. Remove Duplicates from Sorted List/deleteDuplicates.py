"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    #Iterative ad constantly resetting the head with addition of set
    
    new_head = ListNode(-1)
    second = head
    seen = set()
    while second:
        if second.val not in seen:
            seen.add(second.val)
            new_head.next = second
            new_head = new_head.next
            second = second.next
        else:
            second = second.next
    new_head.next = None
    return head