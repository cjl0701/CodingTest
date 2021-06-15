# https://www.acmicpc.net/problem/16234
"""
최소가 아닌데 bfs? : 애초에 bfs는 그래프 탐색 알고리즘!
check를 공유해야 하는 이유: bfs 내에서 또 밟음
O(2000*n^2)
"""
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

# 한번에 bfs를 돌리면 check를 연동해서 쓸 수 있다.
def bfs(a, min_diff, max_diff):
    moved = False
    check = [[False] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            q.append((i, j))
            check[i][j] = True
            nations = [(i, j)]  # list((x, y)) int 나열로 들어간다.. iterable로 list를 만드는 것
            population = a[i][j]
            while q:
                x, y = q.popleft()  # x,y를 바꿔 버린다..
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not check[nx][ny]:
                        if min_diff <= abs(a[x][y] - a[nx][ny]) <= max_diff:
                            q.append((nx, ny))
                            check[nx][ny] = True
                            nations.append((nx, ny))
                            population += a[nx][ny]

            if len(nations) > 1:
                moved = True
                population //= len(nations)
                for x, y in nations:
                    a[x][y] = population
    return moved


n, min_diff, max_diff = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
day = 0
while bfs(a, min_diff, max_diff):
    day += 1
print(day)
