# https://www.acmicpc.net/problem/2003
# 코드가 길고 조건 추가되도 되니 포용적으로.. 그게 안전하고 덜 복잡하다..
n, m = map(int, input().split())
a = list(map(int, input().split()))
start = end = cnt = 0
sum = a[start]
while start <= end and end < n:
    if sum <= m:  # 늘려야
        if sum == m:
            cnt += 1
        end += 1
        if end < n:
            sum += a[end]
    else:  # 줄여야
        sum -= a[start]
        if start == end:
            end += 1
            if end < n:
                sum += a[end]
        start += 1
print(cnt)

