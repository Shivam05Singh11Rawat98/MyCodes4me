class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
             
        color_graph = {}
        for u,v in redEdges:
            if u not in color_graph:
                color_graph[u] = []
            color_graph[u].append((v,'r'))

        for u,v in blueEdges:
            if u not in color_graph:
                color_graph[u] = []
            color_graph[u].append((v,'b'))
        
        output = [-1]*n
        queue = deque([(0,0,None)])
        vis = set()
        while queue:
            m = len(queue)
            node, dist, prevColor = queue.popleft()
            vis.add((node,prevColor))
            if output[node]==-1:
                output[node]=dist
            if node not in color_graph:
                continue
            for neighbor, color in color_graph[node]:
                if (neighbor, color) not in vis and prevColor!=color:
                    queue.append((neighbor,dist+1,color))
        
        return output

"""
redEdges = [[0,1],[1,2]]
blueEdges = []
Output: [0,1,-1]
color_graph:
0-> (1,'r')
1-> (2,'r')
heap = []
new_len = 1
path,node,color = (1,1,'r')
res = [0, 1, -1]
"""


                


        