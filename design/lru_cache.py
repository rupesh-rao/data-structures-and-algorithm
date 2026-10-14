# https://leetcode.com/problems/lru-cache/
# https://takeuforward.org/practice/dsa/lru-cache
class DoubleLinkedList:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity):
        # to store capacity
        self.capacity = capacity
        # to store key to node mapping
        self.map = {}
        # to store head of the linkedlist
        self.head = DoubleLinkedList(-1, -1)
        # to store tail of the linkedlist
        self.tail = DoubleLinkedList(-1, -1)
        # pointing the head and tail to each other next and prev
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        # link the prev and next node of the current node
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_first(self, new_first):
        first = self.head.next
        # point prev and next of new_first node
        new_first.prev = self.head
        new_first.next = first
        # point next and prev of the head and earlier first node
        self.head.next = new_first
        first.prev = new_first

    def get(self, key_):
        if key_ in self.map:
            node = self.map[key_]
            # extract node from its position
            self._remove_node(node)
            # move the node to first
            self._move_to_first(node)
            return node.val
        else:
            return -1

    def put(self, key_, value):
        if key_ in self.map:
            node = self.map[key_]
            node.val = value
            # extract node from its position
            self._remove_node(node)
            # move the node to first
            self._move_to_first(node)
        else:
            if self.capacity == 0:
                lru = self.tail.prev
                # remove from map first because if we extract node first, tail.prev values is changed
                self.map.pop(lru.key)
                self._remove_node(lru)

            node = DoubleLinkedList(key_, value)
            self._move_to_first(node)
            self.map[key_] = node

            if self.capacity > 0:
                self.capacity -= 1



