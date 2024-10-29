```python
def bfs(adj,s):
    parent = [None for _ in adj]
    parent[s] = s
    level = [[s]]
    while len(level[-2]) > 0:
        level.append([])
        for u in level[-2]:
            for v in adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    return parent

def unweighted_shortest_path(adj, s, t):
    parent = bfs(adj,s)
    if parent[t] is None:
        return None
    i=t
    path = [t]
    while i != s :
        i = parent[i]
        path.append(i)

    return path[::-1]


from collections import deque
# BFS 메서드 정의
def bfs (graph, node, visited):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])
    # 현재 노드를 방문 처리
    visited[node] = True
    
    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()
        # 탐색 순서 출력
        print(v, end = ' ')
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
```