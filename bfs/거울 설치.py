# https://www.acmicpc.net/problem/2151
""" 무엇을 정점, 간선으로 볼 것인가 """
""" 포용적으로 짜지 않아서 예외에 걸렸다.
    - a[nx][ny]=='#'일 때 탈출했다면 시작점에 다시 갈때 탈출할 수도 있다.
    - 예제만 봐서 벽이 있을 경우를 고려x
"""
from collections import deque

n = int(input())
a = [list(input()) for _ in range(n)]
door = []
nodes = list()
for i in range(n):
    for j in range(n):
        if a[i][j] in '*.':
            continue
        if a[i][j] == '#':
            door.append(len(nodes))  # 굳이 cnt 변수 유지할 필요 x
        a[i][j] = len(nodes)  # 굳이 dict로 좌표에 해당하는 번호를 찾을 필요 x. 배열에 표시해도 된다.
        nodes.append((i, j))  # 노드로 볼 것만 저장

graph = [list() for _ in range(len(nodes))]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
for x, y in nodes:
    for k in range(4):  # 현재 점으로부터 4방향으로 이동하고 싶으면 이렇게 일반화..
        nx, ny = x + dx[k], y + dy[k]
        while 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == '*':
                break
            if type(a[nx][ny]) == int:
                graph[a[x][y]].append(a[nx][ny])
            nx, ny = nx + dx[k], ny + dy[k]

q = deque()
q.append(door[0])
d = [-1] * len(nodes)
d[door[0]] = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)
print(d[door[1]] - 1)
