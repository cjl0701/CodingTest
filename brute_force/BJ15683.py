# 감시
# 너무 복잡해 => 실수할 확률이 높다
# 간단하게 => 2번 5번은 2,1가지 경우밖에 없지만, 걍 4가지 경우로 통일한다. 수가 크지 않으니.
# 틀린 이유: unmarking 할 때, 중복 마킹한 부분이 지워질 수 있다..
# 효율적인 설계이나 실수하기 좋다. 조금 비효율적이더라도 쉽게 짜자.

dx = (0, 1, 0, -1)  # 동,남,서,북
dy = (1, 0, -1, 0)
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# cctv 갯수, 위치 파악
cctv = list()
for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            cctv.append((i, j, a[i][j]))


def check(b, x, y, dir):
    while 0 <= x + dx[dir] < n and 0 <= y + dy[dir] < m:
        x += dx[dir]
        y += dy[dir]
        if b[x][y] == 6:
            return
        b[x][y] = -1


def count(b):
    cnt = 0
    n, m = len(b), len(b[0])
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt


def go(idx, dirs):
    if idx == len(cctv):
        b = [row[:] for row in a]  # 깊은 복사
        for i, (x, y, no) in enumerate(cctv):
            # 회전 및 체크
            if no == 1:
                check(b, x, y, dirs[i])
            elif no == 2:
                check(b, x, y, dirs[i])
                check(b, x, y, (dirs[i] + 2) % 4)
            elif no == 3:
                check(b, x, y, dirs[i])
                check(b, x, y, (dirs[i] + 1) % 4)
            elif no == 4:
                check(b, x, y, dirs[i])
                check(b, x, y, (dirs[i] + 1) % 4)
                check(b, x, y, (dirs[i] + 2) % 4)
            elif no == 5:
                check(b, x, y, 0)
                check(b, x, y, 1)
                check(b, x, y, 2)
                check(b, x, y, 3)
        return count(b)
    ans = n * m
    # 방향 선택
    for k in range(4):  # 계산하기 쉽게 4개로 통일. 수가 크지 않으므로.
        temp = go(idx + 1, dirs + [k])
        if temp < ans:
            ans = temp
    return ans


print(go(0, []))

"""
def marking(a, i, j, k, mark):  # mark:1 or -1
    nx, ny = i + dx[k], j + dy[k]
    while 0 <= nx < n and 0 <= ny < m and a[nx][ny] != 6:
        a[nx][ny] = mark
        nx += dx[k]
        ny += dy[k]


def count(a):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                cnt += 1
    return cnt


def go(idx, a):
    if idx == len(cctv):
        for row in a:
            print(row)
        print()
        global ans
        ans = min(ans, count(a))
        return
    i, j = pos[idx]
    if cctv[idx] == 1:
        for k in range(4):
            marking(a, i, j, k, -1)
            go(idx + 1, a)
            marking(a, i, j, k, 0)
    elif cctv[idx] == 2:
        for k in range(2):
            marking(a, i, j, k, -1)
            marking(a, i, j, (k + 2) % 4, -1)
            go(idx + 1, a)
            marking(a, i, j, k, 0)
            marking(a, i, j, (k + 2) % 4, 0)
    elif cctv[idx] == 3:
        for k in range(4):
            marking(a, i, j, k, -1)
            marking(a, i, j, (k + 1) % 4, -1)
            go(idx + 1, a)
            marking(a, i, j, k, 0)
            marking(a, i, j, (k + 1) % 4, 0)
    elif cctv[idx] == 4:
        for k in range(4):
            marking(a, i, j, k, -1)
            marking(a, i, j, (k + 1) % 4, -1)
            marking(a, i, j, (k + 2) % 4, -1)
            go(idx + 1, a)
            marking(a, i, j, k, 0)
            marking(a, i, j, (k + 1) % 4, 0)
            marking(a, i, j, (k + 2) % 4, 0)


dx = (-1, 0, -1, 0)  # 북서남동
dy = (0, 1, 0, -1)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = list()  # 하나에 넣어도 됐다..
cctv = list()
for i in range(n):
    for j in range(m):
        ch = arr[i][j]
        if ch == 0 or ch == 6:
            continue
        arr[i][j] = 0
        if ch == 5:
            for k in range(4):
                marking(arr, i, j, k, -1)
        else:
            pos.append((i, j))
            cctv.append(int(ch))

ans = n * m
go(0, arr)
print(ans)
"""
