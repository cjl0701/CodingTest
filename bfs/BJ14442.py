# 벽 부수고 이동하기 2
# 완전 탐색으로 벽을 부수고 시작할 경우, 중복되는 계산이 많다. (1,000,000)^11..
import sys
from collections import deque

# 벽을 부순적이 있는 경우, 없는 경우는 다른 상태이다.
n, m, k = map(int, sys.stdin.readline().split())
arr = [[int(x) for x in sys.stdin.readline().rstrip()] for _ in range(n)]

# k 개의 벽을 지운다.
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
# 상태: x,y,w(벽을 부순 횟수)
d = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
d[0][0][0] = 1
q = deque()
q.append((0, 0, 0))
while q:
    x, y, w = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                if d[nx][ny][w] == -1:
                    d[nx][ny][w] = d[x][y][w] + 1
                    q.append((nx, ny, w))
            else:  # 벽을 부수고 가는 경우
                if w < k and d[nx][ny][w + 1] == -1:
                    d[nx][ny][w + 1] = d[x][y][w] + 1
                    q.append((nx, ny, w + 1))
ans = -1
for i in range(k + 1):
    if d[n - 1][m - 1][i] > 0:
        if ans == -1 or ans > d[n - 1][m - 1][i]:
            ans = d[n - 1][m - 1][i]
print(ans)