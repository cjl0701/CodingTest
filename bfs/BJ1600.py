# 말이 되고픈 원숭이
from collections import deque

dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
dz = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]  # cost
k = int(input())
w, h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
dist = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
dist[0][0][0] = 0
q = deque()
q.append((0, 0, 0))
while q:
    x, y, z = q.popleft()
    # 인접한 곳으로 이동
    for l in range(12):
        nx, ny, nz = x + dx[l], y + dy[l], z + dz[l]
        if 0 <= nx < h and 0 <= ny < w and nz <= k:
            if dist[nx][ny][nz] == -1 and a[nx][ny] == 0:
                dist[nx][ny][nz] = dist[x][y][z] + 1
                q.append((nx, ny, nz))

ans = -1
for z in range(k + 1):
    d = dist[h - 1][w - 1][z]
    if d != -1 and (ans == -1 or ans > d):
        ans = d
print(ans)
