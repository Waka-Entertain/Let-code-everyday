'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        nil = ListNode(0)
        nil.next = head
        curr = nil
        while (curr):
            length +=1
            curr = curr.next
        curr = nil
        length = length - n
        while length>1:
            length -=1
            curr = curr.next
        curr.next = curr.next.next if curr.next else None
        return nil.next
