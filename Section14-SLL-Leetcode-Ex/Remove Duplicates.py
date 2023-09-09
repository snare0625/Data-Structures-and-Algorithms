'''
Remove Duplicates
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):

        nodes = set()

        prev = None
        current = head

        while current:
            if current.value not in nodes:
                nodes.add(current.value)
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = current.next

        return head