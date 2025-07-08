class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = defaultdict(list)
        incount = [0]*numCourses
        for c,prc in prerequisites:
            courseGraph[prc].append(c)
            incount[c]+=1
        
        q = [i for i in range(numCourses) if incount[i]==0]

        count=0
        while q:
            c = q.pop(0)
            count+=1
            for i in courseGraph[c]:
                incount[i]-=1
                if incount[i]==0:
                    q.append(i)
        
        return True if count==numCourses else False
