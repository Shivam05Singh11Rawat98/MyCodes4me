class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construction of Graph
        # calculations
        # gather query output
        div_graph = defaultdict(list)
        for [start,end],value in zip(equations,values):
            div_graph[start].append((end,value))
            div_graph[end].append((start,1/value))
        
        def dfs(start,end,res):
            if start==end:
                return res
            vis.add(start)
            for node,val in div_graph[start]:
                if node not in vis:
                    ans = dfs(node,end,res*val)
                    if ans!=-1.0:
                        return ans
            
            return -1.0
        result=[] 
        for start,end in queries:
            vis = set()
            if start not in div_graph or end not in div_graph:
                result.append(-1)
            else:
                ans = dfs(start,end,1.0)
                result.append(ans)
        
        return result

