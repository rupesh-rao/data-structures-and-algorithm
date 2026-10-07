class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def initialise(self):
        self.arr.clear()
        self.size = 0

    def getMin(self):
        if self.size > 0:
            return self.arr[0]
        else:
            raise Exception("Min heap is empty")

    def heapifyUp(self, index):
        if index > 0:
            parentIndex  = (index-1)//2
            if self.arr[index] < self.arr[parentIndex]:
                self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
                self.heapifyUp(parentIndex)

    def heapifyDown(self, index):
        if index < self.size:
            left = 2*index+1
            right = 2*index+2
            minIndex = index
            if left < self.size and self.arr[left] < self.arr[index]:
                minIndex = left
            if right < self.size and self.arr[right] < self.arr[index]:
                minIndex = right

            if index != minIndex:
                self.arr[index], self.arr[minIndex] = self.arr[minIndex], self.arr[index]
                self.heapifyDown(minIndex)

    def insertElement(self, value):
        self.arr.append(value)
        self.size += 1
        self.heapifyUp(self.size-1)

    def extractMin(self):
        if self.size > 0:
            top = self.arr[0]
            self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
            self.arr.pop()
            self.size -= 1
            self.heapifyDown(0)
            return top
        else:
            raise Exception("Min heap is empty")

    def isEmpty(self):
        return len(self.arr) == 0

    def getSize(self):
        return self.size

    def changeKey(self, index, value):
        oldVal = self.arr[index]
        self.arr[index] = value
        if value < oldVal:
            self.heapifyUp(index)
        else:
            self.heapifyDown(index)

    


