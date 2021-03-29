from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def bfs(a, start, goal):
    n, m = len(a), len(a[0])
    g = a[goal[0]][goal[1]]
    check = [[False] * m for _ in range(n)]
    q = deque()
    q.append(start)
    check[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for k in range(4):  # 이동
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 조사
                if check[nx][ny]:  # 방문 여부 조사
                    continue
                check[nx][ny] = True
                if a[nx][ny] == 1:  # 벽
                    continue
                if a[nx][ny] == g:  # 목표 찾으면 성공
                    return True
                q.append((nx, ny))
    return False


t = int(input())  # 지도의 개수
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]  # 지도
    soma = key = goal = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                goal = (i, j)
            elif a[i][j] == 3:
                soma = (i, j)
            elif a[i][j] == 4:
                key = (i, j)

    # 갈 수 있냐 없냐 => bfs
    if bfs(a, soma, key) and bfs(a, key, goal):
        print(1)
    else:
        print(0)
