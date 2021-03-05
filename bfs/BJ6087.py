# 레이저 통신
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
w, h = map(int, input().split())
a = [input() for _ in range(h)]
sx = sy = ex = ey = -1
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

d = [[-1] * w for _ in range(h)]
d[sx][sy] = 0
q = deque()
q.append((sx, sy))
while q:
    x, y = q.popleft()
    for k in range(4):  # 직선 이동
        nx, ny = x + dx[k], y + dy[k]
        while 0 <= nx < h and 0 <= ny < w and a[nx][ny] != '*':
            if d[nx][ny] == -1: # 이미 도달한 점 갱신하지 않도록
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
            nx += dx[k]
            ny += dy[k]

print(d[ex][ey]-1)
