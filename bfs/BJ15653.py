# 구슬 탈출 4
# 예제는 맞았는데 왜 틀리는데.. 예외 처리 어디가 문제인데.. => arr 그리고 지우는 문제였음.
# 클래스 만들 필요 없다.. 여러 값 반환하면 언패킹 해주거든..
# 원본에 그리는 건 위험하다. 실수 가능성. deepcopy로 복사본 떠서 그리고 버리자..
import copy
from collections import deque


def move(x, y, a, step):
    if a[x][y] == '.':  # 이미 홀에 빠진 상태
        return x, y, False, False
    moved = False
    while True:
        nx, ny = x + step[0], y + step[1]
        ch = a[nx][ny]
        if ch == '#' or ch in 'RB':
            return x, y, False, moved
        elif ch == 'O':
            a[x][y] = '.'  # 구슬을 없앰
            return nx, ny, True, True
        else:
            a[nx][ny], a[x][y] = a[x][y], a[nx][ny]  # swap
            x, y = nx, ny
            moved = True


def simulate(rx, ry, bx, by, a, step):
    a[rx][ry], a[bx][by] = 'R', 'B'
    rhole, bhole = False, False
    while True:
        rx, ry, hole1, rmoved = move(rx, ry, a, step)
        bx, by, hole2, bmoved = move(bx, by, a, step)
        if not rmoved and not bmoved:
            break
        if hole2:
            bhole = True
            break
        if hole1:
            rhole = True

    return rx, ry, bx, by, bhole, rhole  # 알아서 튜플로 패킹!!


steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bx, by = i, j
            arr[i][j] = '.'
# 빨간 구슬과 파란 구슬의 좌표가 상태 => 좌표의 변화가 간선
d = [[[[-1] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # d[ri][rj][bi][bj]
q = deque()
q.append((rx, ry, bx, by))
d[rx][ry][bx][by] = 0
ans = -1
success = False
while q:
    rx, ry, bx, by = q.popleft()
    for step in steps:
        nrx, nry, nbx, nby, bhole, rhole = simulate(rx, ry, bx, by, copy.deepcopy(arr), step)
        if bhole:
            continue
        if rhole:
            ans = d[rx][ry][bx][by] + 1
            success = True
            break
        if d[nrx][nry][nbx][nby] != -1:
            continue
        d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1
        q.append((nrx, nry, nbx, nby))
    if success:
        break
print(ans)
