from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/reverse-linked-list-ii/
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or not head.next:
            return head

        # create dummy node so there always exist a prev node
        dummy = ListNode(-1)
        dummy.next = head

        # find the node before left node
        prev = dummy
        # move `left-1` times to reach node before left
        for i in range(left - 1):
            prev = prev.next

        # left node is next of prev node
        curr = prev.next

        # perform `right-left` times swaps
        # a swap means, insert curr.next after prev
        for i in range(right - left):
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode

        return dummy.next
