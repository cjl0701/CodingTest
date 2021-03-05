# n개 중 m개 고른 수열. 중복 허용
import sys

n, m = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()


def func(idx, arr):
    if idx == m:
        sys.stdout.write(' '.join(map(str, arr)) + "\n")
        return
    for i in range(len(a)):
        func(idx + 1, arr + [a[i]])


func(0, [])
# for r in sorted(set(list(product(a, repeat=m)))):  # m개를 뽑는 모든 순열 (중복 허용)
#     print(' '.join(map(str, r)))
