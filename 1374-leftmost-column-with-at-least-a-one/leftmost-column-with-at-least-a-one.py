# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        lo,hi = 0, cols-1

        while lo <= hi:
            #got the column
            mid = lo + (hi-lo)//2

            flag=0
            for i in range(rows):
                if binaryMatrix.get(i,mid) == 1:
                    flag=1
                    break
            
            if flag==0:
                lo=mid+1
            else:
                hi=mid-1
        

        return lo if lo<cols else -1
                



