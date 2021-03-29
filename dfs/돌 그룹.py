# BJ 12886
import sys

LIMIT = 1500
sys.setrecursionlimit(LIMIT * LIMIT)
check = [[False] * LIMIT for _ in range(LIMIT)]

a, b, c = map(int, input().split())
total = a + b + c


# dfs로 끝까지 가본다.
def dfs(a, b):
    if check[a][b]:
        return
    check[a][b] = True
    # x<y인 i번째와 j번째를 찾아 dfs => 인반화
    now = [a, b, total - a - b]
    for i in range(3):
        for j in range(3):
            if now[i] < now[j]:
                next = [a, b, total - a - b]
                next[i] += now[i]
                next[j] -= now[i]
                dfs(next[0], next[1])


if total % 3 != 0:
    print(0)
else:
    dfs(a, b)
    print(1 if check[total // 3][total // 3] else 0)
