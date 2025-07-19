class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = defaultdict(list)
        req_freq = defaultdict(int)
        for course, pre_req in prerequisites:
            course_graph[pre_req].append(course)
            req_freq[course]+=1
        
        queue = deque()

        for course in range(numCourses):
            if req_freq[course]==0:
                queue.append(course)

        course_count=0
        while queue:
            pre = queue.popleft()
            course_count+=1
            for course in  course_graph[pre]:
                req_freq[course]-=1
                if req_freq[course]==0:
                    queue.append(course)

        return course_count==numCourses


