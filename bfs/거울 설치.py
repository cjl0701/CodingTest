# https://www.acmicpc.net/problem/2151
""" 무엇을 정점, 간선으로 볼 것인가 """
""" 주어진 테케는 맞았으나 예외 처리를 안했다. 실제 시험이었다면 틀린거다..
    - a[nx][ny]=='#'일 때 탈출했다면 시작점에 다시 갈때 탈출할 수도 있다.
    - 예제만 봐서 벽이 있을 경우를 고려x
"""
import sys
from collections import deque

n = int(input())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
nodes = []
start = end = -1
for i in range(n):
    for j in range(n):
        if a[i][j] in '!#':
            if a[i][j] == '#':
                if start == -1:
                    start = len(nodes)
                else:
                    end = len(nodes)
            a[i][j] = len(nodes)
            nodes.append((i, j))

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
graph = [[] for _ in range(len(nodes))]
for frm in range(len(nodes)):
    x, y = nodes[frm]
    for k in range(4):  # 4 방향 for문 돌릴거면 이렇게..
        nx, ny = x + dx[k], y + dy[k]
        while 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == '*':
                break
            if type(a[nx][ny]) == int:
                graph[frm].append(a[nx][ny])
            nx, ny = nx + dx[k], ny + dy[k]

q = deque()
q.append(start)
d = [-1] * len(nodes)
d[start] = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if d[next] == -1:
            d[next] = d[now] + 1
            q.append(next)
print(d[end] - 1)
