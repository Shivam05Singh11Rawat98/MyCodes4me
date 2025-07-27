class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flight_graph = {}
        
        for source, destination, price in flights:
            if source not in flight_graph:
                flight_graph[source]=[]
            flight_graph[source].append((destination, price))
        
        prices = [float('inf')] * n
        print(flight_graph)
        heap = [(0,0,src)]

        while heap:
            pit,cost,city = heappop(heap)

            if pit>k:
                continue
            
            if city not in flight_graph:
                continue
            
            for dest, price in flight_graph[city]:
                new_price = price+cost

                if new_price<prices[dest]:
                    prices[dest]=new_price
                    heappush(heap,(pit+1,new_price,dest))
            
        return prices[dst] if prices[dst] != float('inf') else -1
