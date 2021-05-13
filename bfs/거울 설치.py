# https://www.acmicpc.net/problem/2151
""" 무엇을 정점, 간선으로 볼 것인가 """
""" 포용적으로 짜지 않아서 예외에 걸렸다.
    - a[nx][ny]=='#'일 때 탈출했다면 시작점에 다시 갈때 탈출할 수도 있다.
    - 예제만 봐서 벽이 있을 경우를 고려x
"""
from collections import deque

n = int(input())
a = [input() for _ in range(n)]
door = []
node = dict()
for i in range(n):
    for j in range(n):
        if a[i][j] in '*.':
            continue
        if a[i][j] == '#':
            door.append((i, j))
        node[(i, j)] = len(node)

graph = [list() for _ in range(len(node))]
for x, y in node.keys():
    no = node[(x, y)]
    # 세로 - 이전
    for i in range(x - 1, -1, -1):
        if a[i][y] == '*':
            break
        if a[i][y] in '#!':
            graph[no].append(node[(i, y)])
    # 세로 - 이후
    for i in range(x + 1, n):
        if a[i][y] == '*':
            break
        if a[i][y] in '#!':
            graph[no].append(node[(i, y)])
    # 가로 - 이전
    for j in range(y - 1, -1, -1):
        if a[x][j] == '*':
            break
        if a[x][j] in '#!':
            graph[no].append(node[(x, j)])
    # 가로 - 이후
    for j in range(y + 1, n):
        if a[x][j] == '*':
            break
        if a[x][j] in '#!':
            graph[no].append(node[(x, j)])

q = deque()
q.append(node[door[0]])
d = [-1] * len(node)
d[node[door[0]]] = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)
print(d[node[door[1]]] - 1)
