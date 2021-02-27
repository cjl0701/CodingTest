n = int(input())
arr = list(map(int, input().split()))
d = [0] * n  # d[i]: i번째 고려할 때, 최대 병사 수
d[0] = 1
for i in range(1, n):
    d[i] = d[i - 1]  # 넣지 않는 경우
    # 넣는 경우
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[i]:
            d[i] = max(d[i], d[j] + 1)
            break
print(n - d[n - 1])

# LIS를 활용한 풀이
d = [1] * n  # d[i]: i까지 '넣었을 때', 최대 길이. 따라서 최소 자기 자신 하나 포함.
arr.reverse()  # 가장 긴 증가하는 수열로 풀 것이므로
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))  # d[i] 중 최대값!
