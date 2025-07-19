class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        def distance(x1,y1,x2,y2):
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        
        n = len(bombs)

        for i in range(n):
            for j in range(i+1,n):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                dist = distance(x1,y1,x2,y2)
                if r1>=dist:
                    graph[i].append(j)
                if r2>=dist:
                    graph[j].append(i)
        
        def dfs(node):
            if node in vis:
                return 0
            ans=1
            vis.add(node)
            if node in graph:
                for child in graph[node]:
                    if child not in vis:
                        ans+=dfs(child)
            return ans

        max_bombs = 1
        for node in graph:
            vis = set()
            max_bombs = max(max_bombs,dfs(node))
        
        return max_bombs