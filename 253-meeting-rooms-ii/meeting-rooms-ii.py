class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n==1:
            return 1
        heap=[]
        
        for start,end in sorted(intervals):
            if len(heap)==0 or heap[0]>start:
                heappush(heap,end)
            else:
                heapreplace(heap,end)
        
        return len(heap)
        



