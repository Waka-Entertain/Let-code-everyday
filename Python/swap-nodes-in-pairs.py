'''
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nil = ListNode(None)
        nil.next = head
        prev = nil
        while (prev and prev.next):
            curr = prev.next
            if (curr.next is None):
                prev = curr
                continue
            prev.next = curr.next
            if (curr.next.next is None):
                curr.next = None
            else:
                curr.next = curr.next.next
            prev.next.next = curr
            prev = curr
        return nil.next

print(Solution().swapPairs(ListNode(1,ListNode(2,ListNode(3,ListNode(4))))))