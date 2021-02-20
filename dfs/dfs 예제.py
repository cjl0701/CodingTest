def dfs(graph, v, visitied):
    # 현재 노드를 방문처리
    visitied[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visitied[i]:
            dfs(graph, i, visitied)


# 각 노드가 연결된 정보를 인접 리스트로 표현
graph = [
    [],  # 1번 노드부터 시작
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
