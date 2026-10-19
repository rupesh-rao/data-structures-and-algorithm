# For a node in Doubly LinkedList
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


# For Doubly LinkedList
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeToFront(self, node):
        self.size += 1
        oldFront = self.head.next

        node.next = oldFront
        node.prev = self.head

        self.head.next = node
        oldFront.prev = node

    def removeNode(self, node):
        self.size -= 1
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


class LFUCache:
    def __init__(self, capacity):
        self.maxCapacity = capacity
        self.currCapacity = 0
        self.minFreq = 0
        # stores key to node
        self.keyMap = {}
        # stores freq to LRU doubly linkedlist
        self.freqMap = {}

    def updateFreq(self, node):
        del self.keyMap[node.key]
        # node freq supposed to increase from freq to freq+1
        # remove node from `freq` list (if this freq list is empty and it was the minfreq, then increase minFreq)
        oldFreqList = self.freqMap[node.freq]
        oldFreqList.removeNode(node)

        if oldFreqList.size == 0 and self.minFreq == node.freq:
            self.minFreq += 1

        node.freq += 1
        # add node to `freq+1` list
        freq_list = self.freqMap.get(node.freq, LinkedList())
        # add node to minFreq list
        freq_list.addNodeToFront(node)

        self.freqMap[node.freq] = freq_list
        self.keyMap[node.key] = node

    def get(self, key):
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        value = node.value
        # update the freq of the node
        self.updateFreq(node)
        return value

    def put(self, key, value):
        if self.maxCapacity == 0:
            return
        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            # update the freq of the node
            self.updateFreq(node)
        else:
            if self.currCapacity == self.maxCapacity:
                # fetch the list of min freq nodes
                lfu_list = self.freqMap[self.minFreq]
                # remove the key with min freq and LRU from keyMap
                del self.keyMap[lfu_list.tail.prev.key]
                # remove the key from list
                lfu_list.removeNode(lfu_list.tail.prev)
                # decrease curr capacity
                self.currCapacity -= 1
            # increase curreny capacity
            self.currCapacity += 1
            # create new node
            node = Node(key, value)
            # new nodes sets min freq to 1
            self.minFreq = 1
            # store new key in keyMap
            self.keyMap[key] = node
            # fetch the minFreq list
            freq_list = self.freqMap.get(self.minFreq, LinkedList())
            # add node to minFreq list
            freq_list.addNodeToFront(node)
            # set list to the freqMap
            self.freqMap[self.minFreq] = freq_list



