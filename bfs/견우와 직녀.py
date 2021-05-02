# 문제 조건을 제대로 숙지 못했다.. 그냥 여기에 적어 요약본을..
""" 의문 사항 및 해결 방안
제자리에서 대기하는 경우를 큐에 어떻게 넣는가?
=> 상태가 다르다.
대기 시간을 줄이며 큐에 넣는다. 0이될 때 이동
"""
""" 구현 편의상 올라타서 대기한다고 구현했다 """
""" 조건 요약
1. 한번 지은 오작교는 1분 동안 유지
2. 두번 연속으로 오작교 x
3. 고정 오작교 1개
4. 고정 오작교, 교차하는 곳에 오작교 x
추가 오작교는 하나만 놓을 수 있습니다..
"""
from collections import deque


def bfs():
    # 같은 자리에 있더라도 대기 시간이 다르다. 대기 시간은 0~20
    d = [[[-1] * 20 for _ in range(n)] for _ in range(n)]  # 값=현재 시간
    q = deque()
    q.append((0, 0, 0))
    d[0][0][0] = 0
    while q:
        x, y, cooltime = q.popleft()
        t = d[x][y][cooltime]
        if cooltime > 0:  # 기다림 표현
            if d[x][y][cooltime - 1] == -1:
                d[x][y][cooltime - 1] = t + 1
                q.append((x, y, cooltime - 1))
        else:  # cooltime == 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > 0:
                    if a[x][y] >= 2 and a[nx][ny] >= 2:  # 오작교 두번 연속 못 건넌다
                        continue
                    nct = (a[nx][ny] - (t + 1) % a[nx][ny]) % a[nx][ny]
                    if d[nx][ny][nct] == -1:
                        d[nx][ny][nct] = t + 1
                        q.append((nx, ny, nct))
    return d[n - 1][n - 1][0]


dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
n, ct = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 오작교는 하나만 놓을 수 있다. => 모두 놓아본다
ans = 10 * 10 + 20
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            continue
        a[i][j] = ct
        temp = bfs()
        if temp != -1 and ans > temp:
            ans = temp
        a[i][j] = 0
print(ans)

""" 교차점에 넣어도 의미 없으니 그냥 없이 진행했다. 0이어야 된다는 조건도 애매했고.
나는 4 방향에서 2 방향 이상이면 교차점이라고 했는데, 그럼 가로 2줄도 포함된다.
def can(i,j):
    garo = False
    if j-1 >= 0 and a[i][j-1] == 0:
        garo = True
    if j+1 < n and a[i][j+1] == 0:
        garo = True
    sero = False
    if i-1 >= 0 and a[i-1][j] == 0:
        sero = True
    if i+1 < n and a[i+1][j] == 0:
        sero = True
    return not (garo and sero)
"""
