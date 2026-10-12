from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        prev = None
        curr = head

        while curr:
            # store the next node
            temp = curr.next
            # point current node's next to prev
            curr.next = prev
            # store current node as prev for next iteration
            prev = curr
            # move current node to next node
            curr = temp

        # head at the last prev and current node will be none
        return prev

