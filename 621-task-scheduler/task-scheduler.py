class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = []
        task_cnts = Counter(tasks)
        heap=[-val for val in task_cnts.values()]
        heapify(heap)
        time=0

        while heap or queue:
            val=-1
            if heap:
                val = heappop(heap)
            time+=1
            val+=1
            if val!=0:
                queue.append((val,n+time))
            
            if queue and queue[0][1]==time:
                v,t = queue.pop(0)
                heappush(heap,v)
        
        return time



