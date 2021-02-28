# 가장 긴 감소하는 부분 수열  https://www.acmicpc.net/problem/11722
n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
for i in range(n):  # d[i]가 i에서 시작하는 수열 중 최대 길이라면 거꾸로 구해야 한다!
    for j in range(i):
        if arr[j] > arr[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1

print(max(d))
