"""
 중간에서 만나기 => 탐색의 크기가 줄어든다
 2^40은 너무 커 => 2^20, 2^20은 구할 수 있다.
 반쪽짜리로 two pointers를 쓰든 이진 탐색을 쓰든 방법 수를 줄인다.
"""
# 부분 집합의 합 2
from bisect import bisect_right, bisect_left

n, s = map(int, input().split())
a = list(map(int, input().split()))
m = n // 2
n -= m
first = [0] * (1 << m)
second = [0] * (1 << n)
for bm in range(1 << m):
    for idx in range(m):
        if (bm & (1 << idx)) > 0:
            first[bm] += a[idx]
for bm in range(1 << n):
    for idx in range(n):
        if (bm & (1 << idx)) > 0:
            second[bm] += a[idx + m]

ans = 0
# 이 문제는 two pointers가 더 빠르다. 정렬한 후 선형 탐색하니까.
first.sort()
second.sort()
second.reverse()
idx1 = idx2 = 0
while idx1 < len(first) and idx2 < len(second):
    sum = first[idx1] + second[idx2]
    if sum > s:
        idx2 += 1
    elif sum < s:
        idx1 += 1
    else:
        c1 = c2 = 1
        while idx1 + c1 < len(first) and first[idx1] == first[idx1 + c1]:
            c1 += 1
        while idx2 + c2 < len(second) and second[idx2] == second[idx2 + c2]:
            c2 += 1
        ans += c1 * c2
        idx1 += c1
        idx2 += c2
print(ans if s != 0 else ans - 1)

"""# 이진 탐색으로 구간 찾기
second.sort()
for f in first:
    ans += bisect_right(second, s - f) - bisect_left(second, s - f)
"""
