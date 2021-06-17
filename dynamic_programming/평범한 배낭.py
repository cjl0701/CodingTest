"""
모든 조합을 만들면 2^100.
모든 조합을 알 필요가 없다. 무게별 최대 가치만 유지하면 된다. 거기서 추가! => DP
d: i번째까지 고려했을 때, 무게별 최대 가치. 무게별로 구해야 하는 이유 => 작은 값끼리 더하려고.
d를 어떻게 구하지? for 문으로 무게별로 다 돌려봐야지. bottom-up은 수렴식으로!
"""
n, k = map(int, input().split())
weight, value = zip(*[map(int, input().split()) for _ in range(n)])
weight = [0] + list(weight)
value = [0] + list(value)
"""d = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, k + 1):  # 무게가 0인걸 굳이 포함할 필욘없다.
        # i번째 추가 x
        d[i][w] = d[i - 1][w]
        # i번째 추가
        if w - weight[i] >= 0:
            d[i][w] = max(d[i][w], d[i - 1][w - weight[i]] + value[i])
print(d[n][k])"""

d = [0] * (k + 1)
for i in range(1, n + 1):
    for w in range(k, 0, -1):  # w-weight로 앞놈이 갱신되니까 뒷놈부터 해야한다.
        if w - weight[i] >= 0:
            d[w] = max(d[w], d[w - weight[i]] + value[i])
print(d[k])
