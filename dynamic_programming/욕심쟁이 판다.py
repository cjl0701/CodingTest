# https://www.acmicpc.net/problem/1937
# 접근 방법을 모르겠다.. 완탐은 O(n^4)..dp는 안되는데?
# 문제의 조건, 규칙을 적극 활용하자.. 알고 있는 유형으로만 끼워 맞추려고 하지말고..
import sys

# sys.setrecursionlimit(500 * 500) 계산상으로는 이건데.. 그냥 널널하게 잡자..
sys.setrecursionlimit(10 ** 8)
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def f(x, y):
    if d[x][y] == -1:
        d[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > a[x][y]:
                d[x][y] = max(d[x][y], f(nx, ny) + 1)
    return d[x][y]


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, f(i, j))
print(ans)

"""
# bottom-up: 답이 될 가능성이 적은 높은 수부터 dp 시작
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[1] * n for _ in range(n)]
ans = 0
order = []
for i in range(n):
    for j in range(n):
        order.append((i, j, a[i][j]))
order.sort(key=lambda tp: -tp[2])
for x, y, val in order:
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > a[x][y]:
            d[x][y] = max(d[x][y], d[nx][ny] + 1)
    ans = max(ans, d[x][y])
print(ans)
"""
