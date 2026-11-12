class LinkedListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class ArrayQueue:
    def __init__(self):
        self.head = LinkedListNode(-1)
        self.tail = LinkedListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x):
        newNode = LinkedListNode(x)
        lastNode = self.tail.prev
        # connect newNode with lastNode
        lastNode.next = newNode
        newNode.prev = lastNode
        # connect newNode with tail
        newNode.next = self.tail
        self.tail.prev = newNode

    def pop(self):
        if not self.isEmpty():
            first = self.head.next.val
            # remove head.next by linking head and head.next.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            return first
        return None

    def peek(self):
        if not self.isEmpty():
            return self.head.next.val
        else:
            return None

    def isEmpty(self):
        return self.head.next == self.tail
