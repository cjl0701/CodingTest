# 가장 큰 증가 부분 수열 https://www.acmicpc.net/problem/11055
n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and d[j] > d[i]:
            d[i] = d[j]
    d[i] += arr[i]

print(max(d))
