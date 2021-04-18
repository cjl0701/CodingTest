# https://www.acmicpc.net/problem/14442
""" 벽을 부순적이 있는 경우, 없는 경우는 다른 상태이다 """
import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
n, m, k = map(int, input().split())
a = [sys.stdin.readline().rstrip() for _ in range(n)]
d = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 1
while q:
    i, j, x = q.popleft()
    for dir in range(4):
        ni, nj = i + dx[dir], j + dy[dir]
        if 0 <= ni < n and 0 <= nj < m:
            # 안 부수고 이동
            if a[ni][nj] == '0' and d[ni][nj][x] == -1:
                d[ni][nj][x] = d[i][j][x] + 1
                q.append((ni, nj, x))
            # 부수고 이동
            if a[ni][nj] == '1' and x < k and d[ni][nj][x + 1] == -1:
                d[ni][nj][x + 1] = d[i][j][x] + 1
                q.append((ni, nj, x + 1))

ans = -1
for i in range(k + 1):
    dist = d[n - 1][m - 1][i]
    if dist != -1 and (ans == -1 or ans > dist):
        ans = dist
print(ans)
