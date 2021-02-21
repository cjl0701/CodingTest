# 1~N 중 M개 고른 수열 (중복 선택 허용, 비내림차순)
import sys
from itertools import combinations_with_replacement

n, m = map(int, input().split())
# 비내림차순 -> 순서가 정해짐 -> 조합
# arr = [range(1, n + 1)] # range 객체가 들어감
arr = list(range(1, n + 1))
for c in combinations_with_replacement(arr, m):
    sys.stdout.write(' '.join(map(str, c)) + "\n")


# arr = [0] * m
#
#
# def func(idx, start, n, m):
#     if idx == m:
#         sys.stdout.write(' '.join(map(str, arr)) + "\n")
#         return
#     for i in range(start, n + 1):
#             arr[idx] = i
#             func(idx + 1, i, n, m)
#
#
# func(0, 1, n, m)

# 방법 3: i를 몇 개 골랐는지 담아둔다.
def go(idx, selected, n, m):
    if selected == m:
        for i in range(1, n + 1):  # i를
            for _ in range(cnt[i]):  # cnt[i]번 출력
                sys.stdout.write(str(i) + " ")
        sys.stdout.write("\n")
        return
    if idx > n:
        return
    # idx번째 수를 i개 중복 선택
    for i in range(m - selected, 0, -1):
        cnt[idx] = i
        go(idx + 1, selected + i, n, m)
    # 선택x
    cnt[idx] = 0
    go(idx + 1, selected, n, m)


cnt = [0] * (n + 1)
go(1, 0, n, m)
