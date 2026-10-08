# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow =  head
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
        return fast