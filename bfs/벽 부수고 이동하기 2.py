# BJ 14442
# 벽을 부순적이 있는 경우, 없는 경우는 다른 상태이다.
# 각각의 상태를 큐에 넣고 개별적으로 진행한다.
import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
n, m, k = map(int, sys.stdin.readline().split())
a = [sys.stdin.readline().rstrip() for _ in range(n)]
q = deque()
# 상태: x,y,w(벽을 부순 횟수)
dist = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
dist[0][0][0] = 1
q.append((0, 0, 0))
while q:
    x, y, b = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 뚫을 수 있으면 뚫고 간다
            if a[nx][ny] == '1':
                if b < k and dist[nx][ny][b + 1] == -1:
                    dist[nx][ny][b + 1] = dist[x][y][b] + 1
                    q.append((nx, ny, b + 1))
            else: # 그냥 가는 경우
                if dist[nx][ny][b] == -1:
                    dist[nx][ny][b] = dist[x][y][b] + 1
                    q.append((nx, ny, b))
ans = -1
for i in range(k + 1):
    temp = dist[n - 1][m - 1][i]
    if temp != -1:
        if ans == -1 or ans > temp:
            ans = temp
print(ans)
