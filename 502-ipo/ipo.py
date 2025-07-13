class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        I/P
        k projects
        w initial captial
        profits and captials lists

        O/P - Max Capital
        """

        max_prof = w
        profits = [-1*x for x in profits]
        heap = [(cap,prof) for cap,prof in zip(capital,profits)]
        heapify(heap)
        k=min(k,len(profits))
        max_heap=[]
        while k:
            while heap and heap[0][0]<=max_prof:
                cap,prof = heappop(heap)
                heappush(max_heap,prof)
            if not max_heap:
                return max_prof
            max_prof = max_prof-heappop(max_heap)
            k-=1
        
        return max_prof

            
