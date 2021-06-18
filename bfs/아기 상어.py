# https://www.acmicpc.net/problem/16236
"""
1. 정렬이 무조건 나쁜 건 아니다. 완탐 O(N^2)보단 낫다..
    정렬 기준: 튜플(1순위, 2순위,,,) 오름차순
2. bfs로 함수화하는게 깔끔하다
"""
from collections import deque

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)


def bfs(space, i, j, size):
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    q.append((i, j))
    dist[i][j] = 0
    candidates = list()
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                move = eat = False
                if space[nx][ny] == 0 or space[nx][ny] == size:
                    move = True
                elif 0 < space[nx][ny] < size:
                    move = True
                    eat = True
                if move:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    if eat:
                        candidates.append((dist[nx][ny], nx, ny))
    if candidates:
        candidates.sort()  # x,y 오름차순
        return candidates[0]
    return None


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
i, j = 0, 0
for x in range(n):
    for y in range(n):
        if space[x][y] == 9:
            space[x][y] = 0
            i, j = x, y
t = 0
size = 2
exp = 0
while True:
    result = bfs(space, i, j, size)
    if result is None:
        break
    time, nx, ny = result
    t += time
    space[nx][ny] = 0
    i, j = nx, ny
    exp += 1
    if size == exp:
        size += 1
        exp = 0
print(t)
