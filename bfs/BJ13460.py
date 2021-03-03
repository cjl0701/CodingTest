# 구슬 탈출2

# class Result:
#     def __init__(self, moved, hole, x, y):
#         self.moved = moved
#         self.hole = hole
#         self.x = x
#         self.y = y
LIMIT = 10
dx = (1, 0, -1, 0)  # 북,서,남,동
dy = (0, -1, 0, 1)


def genDir(bm):
    dir = [0] * LIMIT
    for i in range(LIMIT):
        dir[i] = bm & 3
        bm >>= 2
    return dir


def valid(dir):
    for i in range(LIMIT - 1):
        diff = abs(dir[i] - dir[i + 1])
        if diff == 0 or diff == 2:
            return False
        return True


def move(a, d, i, j):
    if a[i][j] == 'O':
        return False, False, i, j
        # return Result(False, False, i, j)
    moved = False
    while True:
        ni, nj = i + dx[d], j + dy[d]
        ch = a[ni][nj]
        if ch == "#" or ch in "RB":
            return moved, False, i, j
        elif ch == 'O':
            a[i][j] = '.'
            return True, True, ni, nj
        else:
            moved = True
            a[i][j], a[ni][nj] = a[ni][nj], a[i][j]  # swap
            i, j = ni, nj


def simulate(dir, ri, rj, bi, bj):
    #a = copy.deepcopy(arr) string으로 받으면 deep copy 할 필요x
    a = [list(row) for row in original]
    for i in range(LIMIT):
        blue_hole = red_hole = False
        while True:
            rmoved, rhole, ri, rj = move(a, dir[i], ri, rj)
            bmoved, bhole, bi, bj = move(a, dir[i], bi, bj)
            if not rmoved and not bmoved:
                break
            if bhole:
                blue_hole = True
                break
            if rhole:
                red_hole = True
        if blue_hole:
            return -1
        if red_hole:
            return i + 1
    return -1


n, m = map(int, input().split())
original = [input() for _ in range(n)]  # str로 받으면 deepcopy할 필요x
ri = rj = bi = bj = 0
for i in range(n):
    for j in range(m):
        if original[i][j] == 'R':
            ri, rj = i, j
        elif original[i][j] == 'B':
            bi, bj = i, j

# 10번 움직이는 경로를 모두 만들고 불가능하면 -1
ans = -1
for bm in range(1 << (2 * LIMIT)):  # 4^10=>2^20
    dir = genDir(bm)
    if valid(dir):  # 의미 있는 이동 경로면 진행
        cur = simulate(dir, ri, rj, bi, bj)
        if cur != -1:  # red hole
            if ans == -1 or ans > cur:
                ans = cur
print(ans)
