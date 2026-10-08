# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# https://takeuforward.org/practice/dsa/clone-a-ll-with-random-and-next-pointer
class Solution:

    def copyRandomList(self, head):
        if not head:
            return head
        curr = head
        # add cloned nodes in between original nodes
        while curr:
            nextNode = curr.next
            curr.next = ListNode(curr.val)
            curr.next.next = nextNode
            if curr.next:
                curr = curr.next.next
            else:
                curr = curr.next

        curr = head
        # populate cloned random nodes for cloned nodes
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        newhead = head.next
        curr1 = head
        curr2 = head.next
        while curr1.next and curr2.next:
            curr1.next = curr1.next.next
            curr2.next = curr2.next.next
            curr1 = curr1.next
            curr2 = curr2.next
        return newhead



