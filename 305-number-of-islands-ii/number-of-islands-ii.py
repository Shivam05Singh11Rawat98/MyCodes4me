class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n
        self.rank = [0] * n
        self.cnt = 0
        self.size = n

    def add_land(self, x):
        if self.parent[x] >=0:
            return
        self.parent[x] = x
        self.cnt+=1
    
    def is_land(self, x):
        if self.parent[x]>=0:
            return True
        return False
    
    def no_of_islands(self):
        return self.cnt

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        # Find roots
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt-=1
"""
parents = [0,0,-1,-1,-1,-1,-1,-1,-1]
rank = [1,0,0,0,0,0,0,0,0]
cnt = 1
pos = 1
"""
#[,,[1,2],[2,1]]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # m*n
        if m==0 or n==0:
            return []
        res=[]
        uf = UnionFind(m*n)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for r,c in positions:
            pos = r*n + c
            uf.add_land(pos)

            for d_x, d_y in directions:
                n_x,n_y = r + d_x, c + d_y
                n_pos = n_x * n + n_y
                if n_x >= 0 and n_x < m and n_y >= 0 and n_y < n and uf.is_land(n_pos):
                    uf.union(pos, n_pos) # O(1), O(1)

            res.append(uf.no_of_islands())
        
        return res

