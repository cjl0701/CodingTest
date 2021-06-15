# 문제의 조건, 규칙을 적극 활용하자.. 알고 있는 유형으로만 끼워 맞추려고 하지말고..
import sys

sys.setrecursionlimit(500 * 500 + 10)
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def f(x, y):
    if d[x][y] == -1:
        d[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and a[x][y] < a[nx][ny]:
                d[x][y] = max(d[x][y], f(nx, ny) + 1)
    return d[x][y]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * n for _ in range(n)]  # d[i][j]: i,j에서 시작해서 살 수 있는 최대 일수
ans = 1
for x in range(n):
    for y in range(n):
        if f(x, y) > ans:
            ans = d[x][y]
print(ans)
