class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        dist_graph = {}
        for edge in edges:
            fro, to, dis = edge
            if fro not in dist_graph:
                dist_graph[fro] = []
            if to not in dist_graph:
                dist_graph[to] = []
            
            dist_graph[to].append((fro,dis))
            dist_graph[fro].append((to,dis))
        
        heap = [(passingFees[0],0,0)] # index, distance and $
        
        last_stop = len(passingFees)-1
        dp = {}
        dp[0]=passingFees[0]
        while heap:
            price, distance, node = heappop(heap)
            if node == last_stop:
                return price
            if (node, distance) in dp and dp[(node, distance)] <= price:
                continue
            dp[(node, distance)] = price
            for to, dist in dist_graph[node]:
                if distance+dist<=maxTime:
                    new_price = price+passingFees[to]
                    heappush(heap,(new_price,distance+dist,to))
        
        return -1


"""
MaxTime=30
passingFees = [5,1,2,20,20,3]
dist_graph = 
1 -> [(2,10)]
2 -> [(1,10), (5,10)]
3 -> [(0,1),(4,10)]
4 -> [(3,10), (5,15)]
5 -> [(2,10), (4,15)]
dp = {0:5, 1:5, 3:25, 2:8, 5:11}
price, distance, node = (11,30,5)
heap = [(20,1,3)]
"""



