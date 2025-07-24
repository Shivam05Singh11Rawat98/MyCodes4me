"""
if there are no elements = [[]]

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        if len(intervals)==0:
            return res 
        res.append(intervals[0])
        for start,end in intervals:
            if res[-1][1]<start:
                res.append([start,end])
            else:
                res[-1][1] = max(end,res[-1][1])
        
        return res
