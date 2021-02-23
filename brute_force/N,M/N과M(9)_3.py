# N개 중 M개 고른 수열 (같은 것을 포함한 순열)
# 원소별 갯수 counting
# Counter: dict의 확장형. key 값에 대한 갯수
import sys
from collections import Counter

n, m = map(int, input().split())
temp = list(map(int, input().split()))
temp = list(Counter(temp).items())  # 중복 제거 & 갯수 count
temp.sort()  # tuple이 들어있는 리스트 => *temp -> tuple들   ex) [(1, 1), (7, 1), (9, 2)]
num, cnt = map(list, zip(*temp))  # 튜플들에 대해 병렬적으로 원소 뽑아서 새 튜플 만듦(1,7,9), (1,1,2) -> 리스트화
arr = [0] * m


def func(idx, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, arr)) + "\n")
        return
    for i in range(n):
        if cnt[i] > 0:
            cnt[i] -= 1
            arr[idx] = num[i]
            func(idx + 1, n, m)
            cnt[i] += 1


func(0, len(num), m)
