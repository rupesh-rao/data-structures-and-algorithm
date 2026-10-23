from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        # left half will be a max heap
        self.left = []
        # right half will be a min heap
        self.right = []

    def addNum(self, num):
        # add num to left half first
        heappush(self.left, -num)
        # remove new max element from left and add it to right half
        heappush(self.right, -heappop(self.left))
        #
        if len(self.left) < len(self.right):
            heappush(self.left, -heappop(self.right))

    def findMedian(self):
        # if both half equal take average of max of left and min of right
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        # if odd size, then median in left half
        else:
            return -self.left[0]