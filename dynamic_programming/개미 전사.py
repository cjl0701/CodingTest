n = int(input())
arr = list(map(int, input().split()))
d = [0] * n  # d[i]: i까지 고려했을 때, 최대 값.
# 선택할 경우와 선택하지 않을 경우로 나뉜다. 예시에 전부 적용해봤으면 알았을 텐데..
d[0], d[1] = arr[0], max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i - 2] + arr[i], d[i - 1])
print(d[n - 1])
