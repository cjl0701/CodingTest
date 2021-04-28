# BJ 14502
# 왜 틀렸는지 모르겠다..
# 디버깅 팁: 찍어서 하나하나 비교해보면 문제를 찾을 수 있다. j가 c~m인게 문제였다.
import copy
from collections import deque

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def bfs(a, i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == '0':
                a[nx][ny] = '2'
                q.append((nx, ny))


# 0의 갯수를 센다
def count_safe_zone(a):
    cur = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '0':
                cur += 1
    return cur


# 임의의 3벽을 세운다.
def build_wall(cnt, arr, r, c):
    if cnt == 3:
        # 2의 bfs
        a = copy.deepcopy(arr)
        for v in virus:
            bfs(a, v[0], v[1])

        global ans
        ans = max(ans, count_safe_zone(a))
        return

    for i in range(r, n):
        for j in range(m):  # for j in range(c, m): 이러면 j가 c~m 사이만 된다..
            if i == r and j < c:  # (i,j) 이후 선택하자. if i == r and j <= c: 이면 (0,0) 선택 못함..
                continue
            if arr[i][j] == '0':
                arr[i][j] = '1'
                build_wall(cnt + 1, arr, i, j)
                arr[i][j] = '0'


n, m = map(int, input().split())
# a = [list(input()) for _ in range(n)] => " "도 원소로 포함된다.
a = [input().split() for _ in range(n)]
virus = list()
for i in range(n):
    for j in range(m):
        if a[i][j] == '2':
            virus.append((i, j))
ans = 0
build_wall(0, a, 0, 0)
print(ans)
