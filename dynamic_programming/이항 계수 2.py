# BJ 11051
import sys

sys.setrecursionlimit(1000) # 재귀 쓸 때 항상..
"""
nCk: n개 중 k개를 고르는 경우의 수.
팩토리얼로 풀면 너무 크다.
다이나믹을 이용할 수 있다.
기준점: n번째. n번째를 선택한 경우 + 선택하지 않은 경우
"""
n, k = map(int, input().split())
c = [[0] * (n + 1) for _ in range(n + 1)]


# c[n][k]: n개 중 k개를 고르는 경우의 수. 0<=k<=n
def f(n, k):
    if k in (0, n):
        return 1
    if c[n][k] == 0:
        c[n][k] = (f(n - 1, k - 1) + f(n - 1, k)) % 10007
    return c[n][k]


print(f(n, k))
