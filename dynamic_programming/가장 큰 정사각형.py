# D를 어떻게 정의하느냐가 정말 중요하다
import sys

n, m = map(int, input().split())
a = ['0' * (m + 1)] + ['0' + sys.stdin.readline().rstrip() for _ in range(n)]
# 가로, 세로, 대각선 방향 모두 1로 채워져야 한다.
# 끝 점에서 (가로, 세로, 대각선) 중 최소 길이를 구하자.
d = [[0] * (m + 1) for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == '1':
            d[i][j] = min(d[i - 1][j], d[i - 1][j - 1], d[i][j - 1]) + 1
        if ans < d[i][j]:
            ans = d[i][j]
print(ans ** 2)
