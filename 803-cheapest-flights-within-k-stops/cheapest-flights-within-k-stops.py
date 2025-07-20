class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flight_graph = defaultdict(list)
        for fro,to,price in flights:
            flight_graph[fro].append((to,price))

        heap = [(0,src,0)] #price,start,stops
        shortest = {(src,0):0}
        while heap:
            price,start,stops = heappop(heap)
            if start==dst:
                return price
            if stops>k:
                continue
            for to,cost in flight_graph[start]:
                new_price = price+cost
                if new_price < shortest.get((to,stops+1),math.inf):
                    shortest[(to,stops+1)] = new_price
                    heappush(heap,(price+cost,to,stops+1))
        
        return -1



            
            
        
