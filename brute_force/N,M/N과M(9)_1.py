# N개 중 M개 고른 수열 (같은 것을 포함한 순열)
# 모든 순열을 구한 뒤 set에 넣어 중복 제거
import sys

n, m = map(int, input().split())
data = list(map(int, input().split()))
arr = [0] * m
check = [False] * n
d = []


def func(idx, n, m):
    if idx == m:
        d.append(tuple(arr))
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        arr[idx] = data[i]
        func(idx + 1, n, m)
        check[i] = False


func(0, n, m)
# s=sorted(s) set 자체 정렬도 가능
d = sorted(list(set(d)))
for v in d:
    sys.stdout.write(' '.join(map(str, v)) + "\n")
