n, m = map(int, input().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
# d[i]: i를 만드는 데 필요한 최소 동전 갯수
# d[i] = min(d[i-k])+1, k는 arr[0-n]
INF = 10001
d = [INF] * (m + 1)
d[0] = 0
for i in range(1, m + 1):
    for k in arr:
        if i - k >= 0 and d[i - k] != INF:
            d[i] = min(d[i], d[i - k])
    if d[i] != INF:
        d[i] += 1
if d[m] == INF:
    print(-1)
else:
    print(d[m])
""" top-down
def f(x):
    if x <= 0:
        return 0
    if d[x] == -1:
        for k in arr:
            if x - k >= 0:
                coin = f(x - k)
                if d[x] == -1 or d[x] > coin:
                    d[x] = coin
        if d[x] != -1:
            d[x] += 1
    return d[x]

d = [-1] * (m + 1)
print(f(m))
"""
