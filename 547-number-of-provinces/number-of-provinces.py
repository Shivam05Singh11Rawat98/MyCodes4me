class unionFind:
    def __init__(self, size):
        self.cnt = size
        self.parent = [x for x in range(0,size+1)]
        self.rank = [1]*(size+1)
    def find(self,i):
        node = self.parent[i]
        if node!=self.parent[node]:
            return self.find(node)
        return node

    def union(self,node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1==root2:
            return
        
        if self.rank[root1]<self.rank[root2]:
            self.parent[root1] = root2
            self.rank[root2] += 1

        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        self.cnt-=1

        
        


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        uf = unionFind(n)


        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    uf.union(i+1,j+1)
        
        return uf.cnt
