# https://www.acmicpc.net/problem/3197
from collections import deque
import sys

"""map이 변할 때, bfs를 이어 실행해 중복을 줄이는 방법 => nq"""

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
r, c = map(int, input().split())
a = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
swan = []
water = deque()
nwater = deque()
q = deque()
nq = deque()
wcheck = [[False] * c for _ in range(r)]
scheck = [[False] * c for _ in range(r)]
# 백조 위치 기록
for i in range(r):
    for j in range(c):
        if a[i][j] == 'L':
            swan.append((i, j))
            a[i][j] = '.'
        if a[i][j] == '.':
            water.append((i, j))

q.append((swan[0][0], swan[0][1]))
scheck[swan[0][0]][swan[0][1]] = True
day = 1

# 얼음이 녹는 것과 백조가 이동하는 것이 별개로 움직임
# 녹이고->움직인다
while True:
    # 얼음인 부분을 큐에 넣고 녹인 후 다음 순서로 넣는다
    while water:
        x, y = water.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and not wcheck[nx][ny]:
                wcheck[nx][ny] = True
                if a[nx][ny] == 'X':
                    a[nx][ny] = '.'  # 얼음을 녹인다
                    nwater.append((nx, ny))

    # 시간 단축을 위해 백조가 얼음을 만나 탐색을 멈추면 다음 큐에 넣고 이어 진행한다.
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and not scheck[nx][ny]:
                scheck[nx][ny] = True
                if a[nx][ny] == '.':
                    q.append((nx, ny))  # 계속 bfs 진행
                else:
                    nq.append((nx, ny))  # 다음 순서로

    if scheck[swan[1][0]][swan[1][1]]:
        print(day)
        break
    day += 1
    water, nwater = nwater, water
    q, nq = nq, q

