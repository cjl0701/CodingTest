# https://www.acmicpc.net/problem/1767
n = int(input())
m = int(input())
k = int(input())

""" 핵심 skill
DP - 문제의 크기를 줄인다.
중복 회피를 위한 case 쪼개기
"""
# 현재 = 이전 * 현재를 만드는 경우의 수
# 변하는 것: n,m,k

# nxm 크기의 체스판에 룩 k를 놓을 수 있는 경우의 수
d = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]


# nxm 크기의 체스판에 룩 k를 놓을 수 있는 경우의 수
def f(n, m, k):
    # end point 이자 base case
    if n < 0 or m < 0 or k < 0:
        return 0
    if k == 0:
        return 1
    if d[n][m][k] == -1:
        # 0개 놓는 경우
        d[n][m][k] += f(n - 1, m, k)
        # 1개 놓는 경우 - 중복 회피를 위해 처음부터 case를 나눠서 따로 구한다
        d[n][m][k] += f(n - 1, m - 1, k - 1) * m  # 위에서 공격 받지 않을 때
        d[n][m][k] += f(n - 2, m - 1, k - 2) * m * (n - 1)  # 위에서 공격 받을 때
        # 2개 놓는 경우
        d[n][m][k] += f(n - 1, m - 2, k - 2) * m * (m - 1) // 2
        d[n][m][k] %= 1000001
    return d[n][m][k]


print(f(n, m, k))
