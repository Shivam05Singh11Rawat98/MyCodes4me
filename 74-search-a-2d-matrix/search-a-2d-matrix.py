class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo,hi=0,len(matrix)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                lo = mid+1
            else:
                hi = mid-1
        
        i=lo-1
        if i<0:
            return False
        lo,hi=0,len(matrix[0])-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            # print(i,mid)
            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]<target:
                lo = mid+1
                
            else:
                hi = mid-1
        
        return False