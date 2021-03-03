# 양
import sys

sys.setrecursionlimit(250 ** 2)
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def dfs(a, x, y):
    v = o = 0
    check[x][y] = True
    ch = a[x][y]
    if ch == 'v':
        v += 1
    elif ch == 'o':
        o += 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c and not check[nx][ny] and a[nx][ny] != "#":
            ret1, ret2 = dfs(a, nx, ny)
            v += ret1
            o += ret2
    return v, o


r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
check = [[False] * c for _ in range(r)]
sheep = wolf = 0

for i in range(r):
    for j in range(c):
        if not check[i][j]:  # 영역 dfs => 영역 내의 v,o 수 세기
            v, o = dfs(a, i, j)
            if v >= o:
                o = 0
            else:
                v = 0
            sheep += o
            wolf += v
print(sheep, wolf)
