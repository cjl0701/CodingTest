# DFS와 BFS
from collections import deque

n, m, start = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for g in graph:
    g.sort()


def dfs(check, v):
    check[v] = True
    print(v, end=" ")
    for next in graph[v]:
        if not check[next]:
            dfs(check, next)


def bfs(check, v):
    q = deque()
    q.append(v)
    check[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for next in graph[v]:
            if not check[next]:
                q.append(next)
                check[next] = True

dfs([False] * (n + 1), start)
print()
bfs([False] * (n + 1), start)
