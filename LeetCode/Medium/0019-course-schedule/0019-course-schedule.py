from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            adj[x].append(y)
        
        visiting=set()
        visited=set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)
            for next in adj[course]:
                if not dfs(next):
                    return False
            visiting.remove(course)
            visited.add(course)
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        
