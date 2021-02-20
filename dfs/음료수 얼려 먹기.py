# 연결 요소를 구하기 위해 dfs 구현
def dfs(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if graph[x][y] == 0:  # 방문하지 않았다면
        graph[x][y] = 1  # 방문 처리
        for step in steps:  # 깊이 우선 탐색으로 방문 처리
            dfs(x + step[0], y + step[1])
        return True
    return False


n, m = map(int, input().split())
# 2차원 리스트 초기화 및 입력 방법
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# visited = [[False for _ in range(m)] for _ in range(n)]
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ans += 1
print(ans)
