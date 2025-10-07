from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            adj[x].append(y)
        
        visited=set()
        
        def dfs(course):
            if course in visited:
                return False
            
            if adj[course] == []:
                return True

            visited.add(course)
            for next in adj[course]:
                if not dfs(next):
                    return False
            visited.remove(course)
            adj[course] = [] 
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        
