# 수직선에서 움직여 땅콩 n개 중 m 개 먹는데 최소 이동 길이
from bisect import bisect_left, bisect_right

n, m, e = map(int, input().split())
arr = list(map(int, input().split()))
cnt = length = 0
idx = bisect_right(arr, e)
if arr[idx] == e:
    cnt += 1
fi, bi = idx, idx - 1
f = b = e
while cnt < m:
    fl = bl = 0
    if fi - 1 >= 0:
        fl = f - arr[fi - 1]
    bl = arr[bi + 1] - b
    if cnt + 1 == m:
        if fl < bl and fl != 0:
            length += fl
            cnt += 1
            fi -= 1
            f = arr[fi]
        else:
            length += bl
            cnt += 1
            bi -= 1
            b = arr[fi]
    else:
        length += fl + bl
        cnt += 2
        fi -= 1
        f = arr[fi]
        bi += 1
        b = arr[bi]
print(length)