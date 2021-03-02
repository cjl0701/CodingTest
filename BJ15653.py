# 구슬 탈출 4
# 예제는 맞았는데 왜 틀리는데.. 예외 처리 어디가 문제인데..
# 클래스 만들 필요 없다.. 여러 값 반환하면 언패킹 해주거든..
# 원본에 그리는 건 위험하다. 실수 가능성. deepcopy로 복사본 떠서 그리고 버리자..
from collections import deque


class Result(object):
    def __init__(self, i, j, moved, hole):
        self.i = i
        self.j = j
        self.moved = moved
        self.hole = hole


steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ri, rj, bi, bj = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ri, rj = i, j
        elif arr[i][j] == 'B':
            bi, bj = i, j
#d = [[[[-1 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]  # d[ri][rj][bi][bj]
d = [[[[-1]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # d[ri][rj][bi][bj]
# d = [[[[-1] * 10] * 10] * 10] * 10  # d[ri][rj][bi][bj]
# print(id(d[0][0])) id가 같다. 곱하기는 list를 단순 복사..
# print(id(d[1][0]))
q = deque()
q.append((ri, rj, bi, bj))
d[ri][rj][bi][bj] = 0
ans = -1


def move(i, j, step):
    if arr[i][j] == '.':  # 이미 홀에 빠진 상태
        return Result(i, j, False, False)
    moved = False
    while True:
        ni, nj = i + step[0], j + step[1]
        ch = arr[ni][nj]
        if ch == '#' or ch == 'R' or ch == 'B':
            return Result(i, j, moved, False)
        elif ch == 'O':
            arr[i][j] = '.'
            return Result(ni, nj, True, True)
        else:  # 이동
            arr[ni][nj] = arr[i][j]
            arr[i][j] = '.'
            i, j = ni, nj
            moved = True


while q:
    ri, rj, bi, bj = q.popleft()
    success = False
    # 이동
    for step in steps:
        arr[ri][rj] = 'R'
        arr[bi][bj] = 'B'
        r_hole, b_hole = False, False
        nri, nrj, nbi, nbj = ri, rj, bi, bj
        while (True):
            red = move(nri, nrj, step)
            blue = move(nbi, nbj, step)
            nri, nrj = red.i, red.j
            nbi, nbj = blue.i, blue.j
            if blue.hole:
                b_hole = True
                break
            if red.hole:
                r_hole = True
            if not blue.moved and not red.moved:
                arr[nri][nrj] = arr[nbi][nbj] = '.' # hole일 수 있는데 이걸..
                break
        if d[nri][nrj][nbi][nbj] != -1:
            continue
        if b_hole:
            continue
        if r_hole:
            ans = d[ri][rj][bi][bj] + 1
            success = True
            break
        d[nri][nrj][nbi][nbj] = d[ri][rj][bi][bj] + 1
        q.append((nri, nrj, nbi, nbj))
    if success:
        break

print(ans)
