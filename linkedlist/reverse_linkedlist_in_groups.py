from __future__ import annotations

# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://takeuforward.org/practice/dsa/reverse-ll-in-group-of-given-size-k
class Solution:
    """
    Use the same idea as reverse linkedlist 2
    """
    def reverseKGroup(self, head, k):
        cnt = 0
        curr = head
        # calculate length of the linkedlist
        while curr:
            cnt += 1
            curr = curr.next
        if cnt <= 1 or k == 1:
            return head

        # create dummy node
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        curr = head
        # do reverse on groups of length k, but skip the group with less than k elements
        for _ in range(cnt // k):
            # reverse operation for a group
            for _ in range(k - 1):
                nextNode = curr.next
                curr.next = nextNode.next
                nextNode.next = prev.next
                prev.next = nextNode
            # move prev to the previous node of the next group of k element
            prev = curr
            curr = curr.next

        return dummy.next


