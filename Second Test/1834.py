import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task = []
        for i,(e,p) in enumerate(tasks):
            task.append([e,p,i])

        task.sort(key=lambda x: x[0])
        
        answer = []
        time = 0
        n = len(task)
        heap = []
        index = 0
        
        while len(answer) < n:
            while index < n and task[index][0] <= time:
                heapq.heappush(heap,(task[index][1],task[index][2]))
                index += 1
            if heap:
                p_t,i = heapq.heappop(heap)
                # print(p_t,i)
                time += p_t
                answer.append(i)
            else:
                time = task[index][0]
                # time += 1
        return answer