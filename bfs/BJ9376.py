# 탈옥 https://www.acmicpc.net/problem/9376
# 그냥 튜플 써도 되는데 굳이 named tuple 쓸 필요x
from collections import deque


def bfs(a, x, y):
    h, w = len(a), len(a[0])
    d = [[-1] * w for _ in range(h)]
    deq = deque()  # 여기에 튜플 넣으면 언패킹됨
    deq.append((x, y))
    d[x][y] = 0
    while deq:
        x, y = deq.popleft()  # 언패킹
        for step in steps:
            nx, ny = x + step[0], y + step[1]
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if a[nx][ny] == '*' or d[nx][ny] != -1:
                continue
            if a[nx][ny] == '#':
                d[nx][ny] = d[x][y] + 1
                deq.append((nx, ny))
            else:
                d[nx][ny] = d[x][y]
                deq.appendleft((nx, ny))
    return d


steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    a = ['.' + input() + '.' for _ in range(h)]
    h += 2
    w += 2
    a = ['.' * w] + a + ['.' * w]  # 리스트 합치기!! a는 str 일차원 리스트

    x1 = y1 = x2 = y2 = -1
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if a[i][j] == '$':
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j

    # 임의의 시작점(0,0), $1, $2로부터 각각 모든 지점까지 거리 구함
    d0 = bfs(a, 0, 0)
    d1 = bfs(a, x1, y1)
    d2 = bfs(a, x2, y2)

    # 거리 합이 최소인 점이 중간지점. (중복 처리)
    ans = h * w
    for i in range(h):
        for j in range(w):
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                cur -= 2
            ans = min(ans, cur)
    print(ans)
