from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        
        for i, eq in enumerate(equations):
            a, b = eq[0], eq[1]
            adj[a][b] = values[i]
            adj[b][a] = 1 / values[i]
        
        def dfs(start, target, visited):
            if start not in adj:
                return -1.0
            
            if target in adj[start]:
                return adj[start][target]
            
            visited.add(start)
            for neighbor, weight in adj[start].items():
                if neighbor not in visited:
                    path_to_target = dfs(neighbor, target, visited)
                    if path_to_target != -1.0:
                        return weight * path_to_target
            
            return -1.0
            


        output=[]
        for start_node, end_node in queries:
            if start_node == end_node and start_node in adj:
                output.append(1.0)
            else:
                result = dfs(start_node,end_node,set())
                output.append(result)



        return output
        