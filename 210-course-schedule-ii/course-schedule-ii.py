class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseGraph = defaultdict(list)
        incount = [0]*numCourses
        for c,prc in prerequisites:
            courseGraph[prc].append(c)
            incount[c]+=1
        
        q = [i for i in range(numCourses) if incount[i]==0]
        res = []
        count=0
        while q:
            c = q.pop(0)
            res.append(c)
            for i in courseGraph[c]:
                incount[i]-=1
                if incount[i]==0:
                    q.append(i)
        
        return res if len(res)==numCourses else []
