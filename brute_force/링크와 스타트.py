# BJ 15661
def go(idx, s, first, second):
    if idx == n:
        if len(first) == 0 or len(second) == 0:
            return -1
        t1 = t2 = 0
        for i1 in first:
            for i2 in first:
                if i1 == i2:
                    continue
                t1 += s[i1][i2]
        for i1 in second:
            for i2 in second:
                if i1 == i2:
                    continue
                t2 += s[i1][i2]
        return abs(t1 - t2)

    ans = -1
    # first.append(idx)
    # ret = go(idx + 1, s, first, second)
    ret = go(idx + 1, s, first + [idx], second)
    if ret != -1 and (ans == -1 or ans > ret):
        ans = ret
    # first.pop()
    ret = go(idx + 1, s, first, second + [idx])
    if ret != -1 and (ans == -1 or ans > ret):
        ans = ret
    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
# first = list()
# second = list()
print(go(0, s, [], []))
