# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next
# https://takeuforward.org/practice/dsa/add-two-numbers-in-ll
class Solution:
    def addTwoNumbers(self, linkedList1, linkedList2):
        """
            :type linkedList1: Optional[ListNode]
            :type linkedList2: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        head = ListNode(-1)
        curr = head
        c = 0

        while linkedList1 and linkedList2:
            s = linkedList1.data + linkedList2.data + c
            d = s % 10
            c = s // 10
            curr.next = ListNode(d)
            linkedList1 = linkedList1.next
            linkedList2 = linkedList2.next
            curr = curr.next
        while linkedList1:
            s = linkedList1.data + c
            d = s % 10
            c = s // 10
            curr.next = ListNode(d)
            curr = curr.next
            linkedList1 = linkedList1.next
        while linkedList2:
            s = linkedList2.data + c
            d = s % 10
            c = s // 10
            curr.next = ListNode(d)
            curr = curr.next
            linkedList2 = linkedList2.next
        if c>0:
            curr.next = ListNode(c)
        return head.next