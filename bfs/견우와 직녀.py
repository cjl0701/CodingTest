# https://www.acmicpc.net/problem/16137
"""
제자리에서 대기하는 경우를 큐에 어떻게 넣는가?
=> 상태가 다르다.
대기 시간을 줄이며 큐에 넣는다. 0이될 때 이동
"""

from collections import deque


# 교차점 검사
def can(i, j):
    garo = sero = False
    if (i - 1 >= 0 and a[i - 1][j] != 1) or (i + 1 < n and a[i + 1][j] != 1):
        sero = True
    if (j - 1 >= 0 and a[i][j - 1] != 1) or (j + 1 < n and a[i][j + 1] != 1):
        garo = True
    return not (garo and sero)


def bfs(a):
    # 같은 자리에 있더라도 대기 시간이 다르다 => 상태 = (i,j,남은 쿨타임)
    d = [[[-1] * 20 for _ in range(n)] for _ in range(n)]
    d[0][0][0] = 0
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, cooltime = q.popleft()
        next_t = d[x][y][cooltime] + 1
        if cooltime > 0:  # 쿨타임 남았을 경우 제자리에서 시간 보낸다
            if d[x][y][cooltime - 1] == -1:
                d[x][y][cooltime - 1] = next_t
                q.append((x, y, cooltime - 1))
        else:  # 아닌 경우 이동
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and a[nx][ny] != 0:
                    if a[x][y] != 1 and a[nx][ny] != 1:
                        continue  # 견우는 두 번 연속으로 오작교를 건너지는 않는다
                    left_t = 0 if next_t % a[nx][ny] == 0 else a[nx][ny] - next_t % a[nx][ny]
                    if d[nx][ny][left_t] == -1:
                        d[nx][ny][left_t] = next_t
                        q.append((nx, ny, left_t))
    return d[n - 1][n - 1][0]


dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 10 * 10 * 20
for i in range(n):
    for j in range(n):
        if a[i][j] == 0 and can(i, j):
            a[i][j] = m  # 직접 표시
            ret = bfs(a)
            if ret != -1 and ret < ans:
                ans = ret
            a[i][j] = 0  # 원상복구
print(ans)
