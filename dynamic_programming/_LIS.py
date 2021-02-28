# 가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053
n = int(input())
arr = list(map(int, input().split()))
d = [1] * n  # 1로 초기화. 자기 자신 포함하는 버전.
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1

print(max(d))
