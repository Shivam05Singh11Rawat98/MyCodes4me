class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        bi_graph = defaultdict(list)

        for person1, person2 in dislikes:
            bi_graph[person1].append(person2)
            bi_graph[person2].append(person1)

        
        color = [-1]*(n+1)
        def dfs(node,par):
            if color[node]!=-1:
                return color[node]==par
            color[node] = par
            for neigh in bi_graph[node]:
                if not dfs(neigh, par^1):
                    return False
            
            return True

        for i in range(1,n+1):
            if color[i]==-1:
                if not dfs(i,1):
                    return False
        
        return True

