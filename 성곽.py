# BJ 2234
# 틀에 갇혀 있었다..
from collections import deque

# 파괴한 구역이 다르면 어떡해? 어떻게 기록해?
# 벽 부수고 이동하기2 => (i,j,부순 벽 갯수)
# 성곽 => (i,j,부순 벽 갯수, 연결 요소) 뚫은 곳이 같은 연결 요소 일수도..
# 그냥 하나씩 없애본다(완탐) - 이전 넓이 활용. 매번 구하는 건 낭비
dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)
m,n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def bfs(destrict, no, i, j):
    destrict[i][j] = no
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            if (a[x][y] & (1 << k)) == 0:  # 이 방향이 벽이 아니면
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and destrict[nx][ny] == -1:
                    destrict[nx][ny] = no
                    q.append((nx, ny))
    return cnt


ans1 = ans2 = ans3 = 0
destrict = [[-1] * m for _ in range(n)]
area = []

for i in range(n):
    for j in range(m):
        if destrict[i][j] == -1:
            area.append(bfs(destrict, ans1, i, j))
            ans2 = max(ans2, area[-1])
            ans1 += 1

# 1,2번 풀이 과정에 얻은 정보를 3번 문제에 활용하기
for i in range(n):
    for j in range(m):
        for k in range(4):
            if (a[i][j] & (1 << k)) != 0:  # 벽이면 뚫어본다
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and destrict[i][j] != destrict[ni][nj]:
                    ans3 = max(ans3, area[destrict[i][j]] + area[destrict[ni][nj]])
print(ans1)
print(ans2)
print(ans3)
