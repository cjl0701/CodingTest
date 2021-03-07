# 뱀
# 고대로 구현하지 않기: 머리를 따라가므로, 시간에 따른 머리의 위치를 기록하면 된다.
import sys

# 게임이 몇 초 만에 끝나는가 / 벽, 몸에 닿으면 끝남

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
n = int(input())
k = int(input())
d = [[-1] * n for _ in range(n)]  # 머리가 위치한 시간
apple = [[False] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    apple[x - 1][y - 1] = True
x = y = direction = 0
l = 1
d[x][y] = now = 0
m = int(input())
# m번 입력 받고 종료까지 while문
for i in range(m + 1):
    t = now + n  # 마지막에 최대 n번 이동 가능
    c = 'temp'
    if i < m:
        t, c = input().split()
        t = int(t)
    # t초 까지 이동
    while now < t:
        now += 1
        # 머리를 먼저 늘린다.
        x += dx[direction]
        y += dy[direction]
        # 벽과 충돌
        if not (0 <= x < n and 0 <= y < n):
            print(now)
            sys.exit(0)
        # 사과가 있다면 길이 증가
        if apple[x][y]:
            apple[x][y] = False
            l += 1
        # 몸과 충돌
        if d[x][y] != -1 and now - d[x][y] <= l:
            print(now)
            sys.exit(0)
        d[x][y] = now

    # t초일 때 방향 바꿈
    if c == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4

"""
from collections import deque

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1
l = int(input())
dirs = deque()
for _ in range(l):
    x, y = input().split()
    dirs.append((int(x), y))

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
d = 0
snake = [(0, 0)]
cnt = 0
rotate = dirs.popleft()


def collision(new_head):
    if not (0 <= new_head[0] < n and 0 <= new_head[1] < n):
        return True
    return new_head in snake


while True:
    # 매초 머리를 늘려 앞으로 전진
    cnt += 1
    new_head = (snake[0][0] + dx[d], snake[0][1] + dy[d])
    # 충돌
    if collision(new_head):
        break
    # 이동
    if arr[new_head[0]][new_head[1]] == 1:  # 사과
        arr[new_head[0]][new_head[1]] = 0
        snake = [new_head] + snake
    else:
        snake = [new_head] + snake[:len(snake) - 1]
    # x초 끝에 회전
    if rotate != -1 and rotate[0] == cnt:
        if rotate[1] == 'L':
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
        if dirs:
            rotate = dirs.popleft()
        else:
            rotate = -1
print(cnt)
"""
