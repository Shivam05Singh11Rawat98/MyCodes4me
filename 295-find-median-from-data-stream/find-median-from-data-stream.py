class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.min_heap,-1*num)

        if self.max_heap and -1*self.min_heap[0]>self.max_heap[0]:
            heappush(self.max_heap,-1*heappop(self.min_heap))


        if len(self.min_heap)-len(self.max_heap)>1:
            ele = heappop(self.min_heap)
            heappush(self.max_heap,-1*ele)

        if len(self.max_heap)-len(self.min_heap)>1:
            ele = heappop(self.max_heap)
            heappush(self.min_heap,-1*ele)

    def findMedian(self) -> float:
        if len(self.min_heap)==len(self.max_heap):
            med = (-self.min_heap[0] + self.max_heap[0])/2
            return med
        else:
            return -1*float(self.min_heap[0]) if len(self.min_heap)>len(self.max_heap) else float(self.max_heap[0])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()