class Solution:
    def __init__(self):
        self.graphMap = defaultdict()
        self.vis = set()
        self.ans=1
    def constGraph(self,equations, values):
        if not equations:
            return
        
        for [start,end],value in zip(equations,values):
            if start not in self.graphMap:
                self.graphMap[start] = [(end,value)]
            else:
                self.graphMap[start].append((end,value))
            if end not in self.graphMap:
                self.graphMap[end] = [(start,1/value)]
            else:
                self.graphMap[end].append((start,1/value))
            
            
    def calEquationHelper(self,start,end,val,vis):
        vis.add(start)
        if start==end:
            return val
        ans = 1
        for next,wt in self.graphMap[start]:
            if next not in vis:
                ans = self.calEquationHelper(next,end,val*wt,vis)
                if ans!=-1:
                    return ans

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.constGraph(equations,values) #constructing the Graph (bi-direct)
        if not self.graphMap:
            return []
        res = []
        for start,end in queries:
            if start in self.graphMap and end in self.graphMap:
                vis = set()   
                res.append(self.calEquationHelper(start,end,1.0,vis))
            else:
                res.append(float(-1))
        
        return res

