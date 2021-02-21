# 부분 수열의 합
# 비트마스크 => 모든 조합 만들기
# 비트마스크보다 combinations가 더 빠르다
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
# for set in range(1, 1 << n):
#     _sum = sum([arr[idx] for idx in range(len(arr)) if set & (1 << idx)])
#     if _sum == s:
#         cnt += 1

for i in range(1, n + 1):
    for c in list(combinations(arr, i)):  # arr에서 i개를 선택하는 모든 조합
        if sum(c) == s:
            cnt += 1

print(cnt)
