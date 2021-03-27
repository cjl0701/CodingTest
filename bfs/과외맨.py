# BJ 5213
# 메인 함수에 실수(or 초반 착각)가 있을 수도 있다.. 주석 달아 설계를 해야 실수를 덜한다.
from collections import deque

# 짝수일 때, 홀수일 때 다르다!!
dx = [(-1, -1, 0, 0, 1, 1), (-1, -1, 0, 0, 1, 1)]
dy = [(-1, 0, -1, 1, -1, 0), (0, 1, -1, 1, 0, 1)]

n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
    lim = n if i % 2 == 0 else n - 1
    for _ in range(lim):
        a[i].append(tuple(map(int, input().split())))
d = [[-1] * n for _ in range(n)]
via = [[-1] * n for _ in range(n)]
q = deque()
q.append((0, 0))
d[0][0] = 1

# 수로 규칙 찾기보다 그림으로 규칙 찾기가 좋다
def num(x, y):
    no = n * x - x // 2
    return no + y + 1


def ok(x, y):
    lim = n if x % 2 == 0 else n - 1
    return 0 <= x < n and 0 <= y < lim


def possible(x, y, nx, ny):
    if x % 2 == 0:
        if y <= ny:
            return a[x][y][1] == a[nx][ny][0]
        else:
            return a[nx][ny][1] == a[x][y][0]
    else:
        if y < ny:
            return a[x][y][1] == a[nx][ny][0]
        else:
            return a[nx][ny][1] == a[x][y][0]


while q:
    x, y = q.popleft()
    for k in range(6):
        nx, ny = x + dx[x % 2][k], y + dy[x % 2][k]  # no%2이라고해서 틀림.. 발견 못함. 함수가 틀린줄..
        if not ok(nx, ny):
            continue
        if d[nx][ny] != -1:
            continue
        if possible(x, y, nx, ny):
            d[nx][ny] = d[x][y] + 1
            q.append((nx, ny))
            via[nx][ny] = (x, y)
# 방문한 것 중 번호가 가장 큰 타일
x = y = n - 1
while d[x][y] == -1:  # 중간에 탈출할거면 이중 for문보다 while
    y -= 1
    if y < 0:
        x -= 1
        y = n - 1 if x % 2 == 0 else n - 2
print(d[x][y])
l = list()
while not (x == 0 and y == 0):  # 출발지점까지
    l.append((x, y))
    x, y = via[x][y]
l.append((0, 0))
while l:
    print(num(*l[-1]), end=" ")
    l.pop()

"""
n = int(input())
q = deque()
length = n * n - n // 2 + 1
dist = [-1] * length
frm = [-1] * length
arr = [list(map(int, input().split())) for _ in range(length - 1)]
arr = [[0, 0]] + arr
d = (-n, -n + 1, -1, 1, n - 1, n)
idx = ((0, 1), (1, 0), (0, 1), (1, 0), (0, 1), (1, 0))
# 시작점으로부터 최소 이동 비용을 기록

q.append(1)
dist[1] = 0
while q:
    t = q.popleft()
    # 이동
    for k in range(6):
        nt = t + d[k]
        if not 1 <= nt < length: # 요 범위가 틀렸다.. 라인으로 표현해야..?
            continue
        if dist[nt] == -1 and arr[t][idx[k][0]] == arr[nt][idx[k][1]]:
            q.append(nt)
            dist[nt] = dist[t] + 1
            frm[nt] = t

tile = length - n - 1
for t in range(length - 1, length - n, -1):
    if dist[t] != -1:
        tile = t
        break
ans = list()
while tile != -1:
    ans.append(tile)
    tile = frm[tile]
ans.reverse()
print(' '.join(map(str, ans)))
print(dist)
print(frm)
"""
