# 돌 그룹
# bfs,dfs 문제를 dp로 풀었다. 근데 풀이를 보면 거의 dfs다.. 이전 답을 활용하고 있지 않다.
# 있냐 없냐 => bfs. 최소가 존재한다면 있고 없다면 없는 것. => 최소 구하는 게 아니면 dfs도 가능. 도달할 수 있는가?
""" 왜 틀렸는지 모르겠다. 예외를 못 찾겠다.
0. '예외 케이스'를 찾기 어렵다면 논리적으로 찾아라. 가정해가며.
1. 예외를 못 찾았어도 논리가 잘못된 걸 찾았어야 했다. 한 줄 한 줄..
2. 랜덤 돌려서 찾아냈다.
"""

import sys

sys.setrecursionlimit(1500 * 1500)
a, b, c = map(int, input().split())
LIMIT = 1501
import random
# a, b, c = [random.randrange(1, 501) for _ in range(3)]
check = [[False] * LIMIT for _ in range(LIMIT)]  # d[a][b]: a,b인 상태가 될 수 있냐 없냐
s = a + b + c


def go(a, b):
    print(a, b)
    if check[a][b]:
        return
    check[a][b] = True
    now = [a, b, s - a - b]
    for i in range(3):
        for j in range(3):
            if now[i] < now[j]:  # X < Y
                next = [a, b, s - a - b]
                next[i] += now[i]
                next[j] -= now[i]
                # if next[i] < LIMIT and next[j] >= 0: # 제한을 넘거나 음수가 되지 않는다..
                go(next[0], next[1])


if s % 3 != 0:
    print(0)
else:
    go(a, b)
    print(1 if check[s // 3][s // 3] else 0)
"""
a, b, c = map(int, input().split())
LIMIT = 501
d = [[[-1] * LIMIT for _ in range(LIMIT)] for _ in range(LIMIT)]
# d[a][b][c]: a,b,c 개일 때, a==b==c가 되는 경로가 있는가


def f(a, b, c):
    if a == b == c:
        d[a][b][c] = 1
        return 1
    if d[a][b][c] != -1:
        return d[a][b][c]
    d[a][b][c] = 0
    # A-B  # 아래 몇 십줄 짜리 코드를 반복문으로 단 8줄 만에 할 수 있었다..
    x, y = a, b
    if x > y:
        x, y = y, x
    if x + x <= LIMIT and y - x >= 0:
        if x == a:
            if f(x + x, y - x, c) == 1:
                d[a][b][c] = 1
                return d[a][b][c]
        else:
            if f(y - x, x + x, c) == 1:
                d[a][b][c] = 1
                return d[a][b][c]
    # B-C
    x, y = b, c
    if x > y:
        x, y = y, x
    if x + x <= LIMIT and y - x >= 0:
        if x == b:
            if f(a, x + x, y - x) == 1:
                d[a][b][c] = 1
                return d[a][b][c]
        else:
            if f(a, y - x, x + x) == 1:
                d[a][b][c] = 1
                return d[a][b][c]
    # C-A
    x, y = c, a
    if x > y:
        x, y = y, x
    if x + x <= LIMIT and y - x >= 0:
        if x == a:
            if f(x + x, b, y - x) == 1:
                d[a][b][c] = 1
                return d[a][b][c]
        else:
            if f(y - x, b, x + x) == 1:
                d[a][b][c] = 1
                return d[a][b][c]

    return 0

print(f(a, b, c))
"""
