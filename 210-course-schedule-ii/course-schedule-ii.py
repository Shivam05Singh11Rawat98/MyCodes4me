"""
course_graph
0->1,2
1->3
2->3
depend_freq
0:0
1:0
2:0
3:0
queue:

course_order = [0,1,2,3]
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        no_course=0
        course_order = []
        depend_freq = defaultdict(int)
        course_graph = defaultdict(list)

        for course, pre in prerequisites:
            course_graph[pre].append(course)
            depend_freq[course]+=1
        
        queue = deque()

        for course in range(numCourses):
            if depend_freq[course]==0: 
                queue.append(course)
        
        while queue:
            pre = queue.popleft()
            course_order.append(pre)
            no_course+=1
            for course in course_graph[pre]:
                depend_freq[course]-=1
                if depend_freq[course]==0:
                    queue.append(course)


        return course_order if no_course==numCourses else []