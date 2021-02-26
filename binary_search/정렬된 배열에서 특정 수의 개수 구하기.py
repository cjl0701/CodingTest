# 정렬된 배열이 주어지고, log 시간만에 찾아야 함.
from bisect import bisect_left, bisect_right


def count_by_range(arr, left_value, right_value):
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)


n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = count_by_range(arr, x, x)
if ans == 0:
    ans = -1
print(ans)
