# 틀린 이유 : 반대편의 최대값을 구해야 했다..

import sys

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0


def go(a, r, c, s):
    if r == c == 1:
        global ans
        ans = max(ans, s)
        return
    # 세로 자르기 1
    nc = c // 2
    if nc > 0:
        na = [row[:nc] for row in a]
        temp = 0
        for i in range(r):
            for j in range(nc, c):
                if temp < a[i][j]:
                    temp = a[i][j]
        go(na, r, nc, s + temp)
    # 세로 자르기 2
    nc = c // 2
    if nc > 0:
        na = [row[nc:] for row in a]
        temp = 0
        for i in range(r):
            for j in range(nc):
                if temp < a[i][j]:
                    temp = a[i][j]
        go(na, r, nc, s + temp)

    # 가로 자르기 1
    nr = r // 2
    if nr > 0:
        na = [a[i][:] for i in range(nr)]
        temp = 0
        for i in range(nr,r):
            for j in range(c):
                if temp < a[i][j]:
                    temp = a[i][j]
        go(na, nr, c, s + temp)

    # 가로 자르기 2
    nr = r // 2
    if nr > 0:
        na = [a[i][:] for i in range(nr, r)]
        temp = 0
        for i in range(nr):
            for j in range(c):
                if temp < a[i][j]:
                    temp = a[i][j]
        go(na, nr, c, s + temp)


go(a, n, n, 0)
print(ans)
