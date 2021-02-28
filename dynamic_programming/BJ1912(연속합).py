# 연속합 https://www.acmicpc.net/problem/1912
n = int(input())
arr = list(map(int, input().split()))
d = arr.copy()  # d[i]: i까지 포함했을 때 최대 합. d[i]=max(d[i-1]+arr[i](연속), arr[i](새시작)
for i in range(1, n):
    if d[i] < d[i - 1] + arr[i]:  # 틀린 이유: 파이썬은 d[-1]이 d[n-1]이다..
        d[i] += d[i - 1]
print(max(d))
