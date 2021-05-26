# https://www.acmicpc.net/problem/16987
# 경우의수 제대로 계산해라. 그 과정이 코드로 그대로 구현되는 경우가 많다.  (n-1)^n
""" 피드백
전역변수 쓰지 않고 그냥 끝에서 구한 값을 리턴해줘도 된다
n이 작으니까 그냥 cnt를 맨 끝에서 직접 구해도 된다
탈출 조건을 2가지 경우로 처리해도 되지만, 다음으로 진행하지 않을 경우를 위한 flag를 둬도 된다.
"""
n = int(input())
d = [0] * n
w = [0] * n
for i in range(n):
    d[i], w[i] = map(int, input().split())


def go(idx):
    if idx == n:
        # n이 작으므로 끝에서 세버린다 (구현하기 쉽게)
        broken = 0
        for durability in d:
            if durability <= 0:
                broken += 1
        return broken

    if d[idx] <= 0:
        return go(idx + 1)

    ans = 0
    all_broken = True
    for i in range(n):
        if i == idx or d[i] <= 0:
            continue
        d[i] -= w[idx]
        d[idx] -= w[i]
        all_broken = False
        ans = max(ans, go(idx + 1))
        d[i] += w[idx]
        d[idx] += w[i]

    # 다 깨져서 안으로 다음으로 넘어가지 못하는 경우가 있다.
    if all_broken:
        return go(n)

    return ans


print(go(0))
