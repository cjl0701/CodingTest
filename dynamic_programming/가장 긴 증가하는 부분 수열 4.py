# https://www.acmicpc.net/problem/14002
n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
from_idx = [-1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
            from_idx[i] = j

ans = max(d)
print(ans)
# 인덱스 알아내는 법
idx = [i for i, x in enumerate(d) if x == ans][0]  # 반복문을 한 줄에 쓰기 위해


def go(idx):
    if idx == -1:
        return
    go(from_idx[idx])
    print(arr[idx], end=" ")


go(idx)
