# 평범한 배낭  https://www.acmicpc.net/problem/12865
# 가치 최대합 => 완탐 or DP / n<=100, 완탐 가짓수 2^100.. 최대값만 기록하면 되므로 DP!
# i번째까지 고려했을 때, 무게 w일때 가치 v => d[i][w]=v
# i번째 선택, 선택x 무게별 최대 가치만 알고 있으면 된다.

n, k = map(int, input().split())
# d[i]는 d[i-1]를 이용해 계산하므로, i는 1부터 시작하는 것으로 구한다.
w, v = zip(*[list(map(int, input().split())) for _ in range(n)])
w = [0] + list(w)
v = [0] + list(v)
# for i in range(n):
#     w[i], v[i] = map(int, input().split())

# 고대로 내려오거나, 갱신 -> 일차원 배열로
d = [0] * (k + 1)
for i in range(1, n + 1):
    for j in range(k, 0, -1):  # 역순으로 구해야 한다.
        if j - w[i] >= 0:
            d[j] = max(d[j], d[j - w[i]] + v[i])  # 앞 값으로 갱신하므로 j를 중복 선택하므로
print(max(d))
""" 파이썬3는 시간 초과.. 시간을 더 줄이려면? 이차원 배열을 그려 방법을 찾아보자
d = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        d[i][j] = d[i - 1][j]  # i번째를 선택하지 않았을 경우
        if j - w[i] >= 0:  # i번째 선택
            d[i][j] = max(d[i][j], d[i - 1][j - w[i]] + v[i])

print(max(d[n]))
"""
