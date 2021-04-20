# https://www.acmicpc.net/problem/1767
n = int(input())
m = int(input())
k = int(input())

"""
DP로 문제의 크기를 줄여가 본다.
현재 = 이전 * 현재를 만드는 경우의 수
"""
# 변하는 것: r,c,k
# 케이스 나누기 복잡 => 좀 더 큰 관점으로, 임의의 기준을 잡는다.

d = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]


# r,c:선택할 수 있는 칸의 갯수 / x:남은 룩의 갯수
def f(r, c, x):
    # end point 이자 base case
    if x == 0:
        return 1
    if r <= 0 or c <= 0 or x < 0:
        return 0
    if d[r][c][x] == -1:
        d[r][c][x] = 0
        # 0개 놓는 경우
        d[r][c][x] += f(r - 1, c, x)
        # 1개 놓는 경우
        d[r][c][x] += f(r - 1, c - 1, x - 1) * c  # 위에서 공격 받지 않을 때
        d[r][c][x] += f(r - 2, c - 1, x - 2) * c * (r - 1)  # 위에서 공격 받을 때
        # 2개 놓는 경우
        d[r][c][x] += f(r - 1, c - 2, x - 2) * c * (c - 1) // 2
        d[r][c][x] %= 1000001
    return d[r][c][x]


print(f(n, m, k))
