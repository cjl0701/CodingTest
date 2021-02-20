from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
q = deque()  # q = deque((0, 0))는 iterable 데이터를 하나하나 넣는 것 ->int형 덱
q.append((0, 0))  # 튜플 데이터를 담을 수 있다.
# visited = [[False for _ in range(m)] for _ in range(n)]
d = [[0 for _ in range(m)] for _ in range(n)]
d[0][0] = 1
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
# q.append(1) 이걸 넣는 순간 int 형이됨. pop시 에러. q.append(('a','b') 처럼 튜플을 넣는 건 가능

while q:
    x, y = q.popleft()  # 튜플을 꺼내 언패킹
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m): continue
        if graph[nx][ny] == 0: continue
        if not d[nx][ny] == 0:
            d[nx][ny] = d[x][y] + 1
            q.append((nx, ny))

print(d[n - 1][m - 1])
