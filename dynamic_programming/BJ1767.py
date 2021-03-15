# N-Rook II
# 문제의 크기를 줄인다.
# 케이스 나누기 복잡 => 좀 더 큰 관점으로, 임의의 기준을 잡는다.
n = int(input())
m = int(input())
k = int(input())
d = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]


def f(n, m, k):
    if k == 0:
        return 1
    if k < 0 or n <= 0 or m <= 0:
        return 0
    # if n == 1: # 위에 다 포함된다
    #     if k == 1:
    #         return m
    #     elif k == 2:
    #         return m * (m - 1) // 2
    #     else:
    #         return 0
    # if m == 1:
    #     if k == 1:
    #         return n
    #     elif k == 2:
    #         return n * (n - 1) // 2
    #     else:
    #         return 0

    if d[n][m][k] == -1:
        d[n][m][k] = f(n - 1, m, k) + f(n - 1, m - 1, k - 1) * m \
                     + f(n - 2, m - 1, k - 2) * m * (n - 1) + f(n - 1, m - 2, k - 2) * (m * (m - 1) // 2)
        d[n][m][k] %= 1000001
    return d[n][m][k]


print(f(n, m, k))
