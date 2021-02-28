# 가장 긴 바이토닉 부분 수열 https://www.acmicpc.net/problem/11054
n = int(input())
arr = list(map(int, input().split()))
di = [1] * n  # i에서 끝나는 가장 긴 증가 부분 수열
dd = [1] * n  # i에서 시작하는 가장 긴 감소 부분 수열

# 가장 긴 증가 부분 수열
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and di[j] + 1 > di[i]:
            di[i] = di[j] + 1
# 가장 긴 감소 부분 수열
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j] and dd[i] < dd[j] + 1:
            dd[i] = dd[j] + 1

# 가장 긴 바이토닉 부분 수열
d = [di[i] + dd[i] - 1 for i in range(n)]  # 리스트 컴프리헨션: 리스트를 반복문으로 만드는 빠르고 편리한 방법

print(max(d))
