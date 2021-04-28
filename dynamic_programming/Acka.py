# BJ 12996
# top down은 불필요한 연산을 안해서 더 빠를 것
MOD = 1000000007
s, x, y, z = map(int, input().split())
# d[i][a][b][c]: i번째 곡, 부른 횟수
d = [[[[-1] * (z + 1) for _ in range(y + 1)] for _ in range(x + 1)] for _ in range(s + 1)]


def f(n, a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0
    if n == 0:
        return 1 if a == b == c == 0 else 0
    if d[n][a][b][c] == -1:
        d[n][a][b][c] = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if i == j == k == 0:
                        continue
                    d[n][a][b][c] += f(n - 1, a - i, b - j, c - k)
        d[n][a][b][c] %= MOD # 최대 MOD의 7배니까 한번에 나눠도 괜찮은 수
    return d[n][a][b][c]


print(f(s, x, y, z))

"""bottom-up
case = ((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1))
s, x, y, z = map(int, input().split())
d = [[[[0] * 51 for _ in range(51)] for _ in range(51)] for _ in range(51)]
d[0][x][y][z] = 1  # d[i][a][b][c]: i번째 곡, a,b,c 인 경우의 수
for i in range(s):
    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                for k in case:
                    if a - k[0] >= 0 and b - k[1] >= 0 and c - k[2] >= 0:
                        d[i + 1][a - k[0]][b - k[1]][c - k[2]] += d[i][a][b][c]
                        d[i + 1][a - k[0]][b - k[1]][c - k[2]] %= MOD
print(d[s][0][0][0])
"""
