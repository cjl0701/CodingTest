# https://www.acmicpc.net/problem/16234
"""
최소가 아닌데 bfs? : 애초에 bfs는 그래프 탐색 알고리즘!
check를 공유해야 하는 이유: bfs 내에서 또 밟음
O(2000*n^2)
"""
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


# 이렇게 하면 check도 바로 연동됨
def bfs(a, l, r):
    n = len(a)
    check = [[False] * n for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                q = deque()
                q.append((i, j))
                check[i][j] = True
                union = []
                population = 0
                while q:
                    x, y = q.popleft()
                    union.append((x, y))
                    population += a[x][y]
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not check[nx][ny]:
                            if l <= abs(a[x][y] - a[nx][ny]) <= r:
                                check[nx][ny] = True
                                q.append((nx, ny))

                if len(union) > 1:
                    population //= len(union)
                    for x, y in union:
                        a[x][y] = population
                    moved = True
    return moved


# 뼈대부터 만들어라. 그래야 길을 잃지 않아.
ans = 0
while True:
    if bfs(a, l, r):
        ans += 1
    else:
        break
print(ans)
