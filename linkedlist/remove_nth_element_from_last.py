# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # return if head is None
        if head is None:
            return head
        curr = head
        i = 0
        # move n steps
        while i < n:
            curr = curr.next
            i += 1
        # if curr reached None
        # meane first element is Nth last
        if curr is None:
            return head.next

        pre = None
        last = head
        # move last till the curr reaches None
        while curr:
            curr = curr.next
            pre = last
            last = last.next
            # remove the last node
        pre.next = last.next
        return head




