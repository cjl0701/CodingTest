import sys

sys.setrecursionlimit(100100)
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [-1] * n


def f(idx, n, a, d):
    if idx < 0 or idx >= n:  # 실패
        return 0

    if d[idx] == -2:  # 밟은 곳 또 밟음 -> 무한 회로
        cnt = 1
        start = idx
        while True:  # 다시 돌아올 때까지 count
            next = idx + a[idx]  # 이동
            if next == start:  # 다시 돌아옴
                break
            cnt += 1
            idx = next
        return cnt  # 이전에 호출했던 d[idx]에서 cnt 기록 됨

    if d[idx] == -1:  # 첫 방문
        d[idx] = -2  # 밟음 표시
        d[idx] = f(idx + a[idx], n, a, d)
    return d[idx]


for start in range(n):
    f(start, n, a, d)
print(max(d))
