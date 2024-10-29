# MIT

```python
def dfs(adj,s,parent=None,order=None):
    if parent is None:
        parent = [None for _ in adj]
        parent[s] = s
        order=[]
    for v in adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(adj,v,parent,order)
    order.append(s)
    return parent, order
```

# 일반 블로그

```python
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
	[],  # idx 0 은 사용하지 않기 위함
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6,  8],
	[1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9  # idx 0 은 사용하지 않기 위해 9(8+1)로 초기화함

# DFS 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end=' ')
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)  # 실행결과: 1 2 7 6 8 3 4 5

```