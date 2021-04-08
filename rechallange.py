# BJ 12970
from collections import Counter

n, k = map(int, input().split())
ans = ""


def go(max, left, sum, l):
    if left == 0:
        if sum == k:
            counter = Counter(l)
            return True
        return False
    for i in range(max):
        if go(len, left - 1, sum + i, l + [i]):
            return True
    return False


for b in range(n):
    if go(b, n - b, 0, []):
        print(ans)
        exit(0)
print(-1)
