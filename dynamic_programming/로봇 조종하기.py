# https://www.acmicpc.net/problem/2169
"""
순환 참조로 인한 무한 반복 해결법
1. 순서를 정한다.
2. 이전 방향을 기록해 순환 참조를 배제한다.
"""
""" 방황의 기록
순서를 매겨보려고 했다.
for문을 3번 돌린다면 방문한 곳을 또 방문하는데?라고 생각했다.
그런데 for문이라면 어차피 횟수가 정해져있다.
재귀일 경우 check로 중복 재귀를 막아야 하는 것.

재귀로 d[i][j]=max(d[i-1][j], d[i][j-1], d[i][j+1])+a[i][j]를 풀 경우엔 무한 재귀에 빠진다.
그럼 for문으로 풀면되지. 순서를 임의로 정하면 된다.

라고 생각했는데.. d[i+1][j]로 d[i][j]를 구하는 경우, a[i][j]가 이미 포함되어있을 수 있다..
따라서 어디서 왔는지도 기록해야 한다.

정리
1. 재귀로 가면 무한 재귀에 빠진다 -> for문으로 간다
2. 이전에 어떤 방향으로 왔느냐에 따라서 불가능한 경우 -> 상태 분류 
"""
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
d = [[[-INF] * 3 for _ in range(m)] for _ in range(n)]
# d[i][j][k]: i,j에 k 방향으로 온 경우 최대값
d[0][0][1] = a[0][0]
for j in range(1, m):
    d[0][j][1] = d[0][j - 1][1] + a[0][j]

for i in range(1, n):
    # 0,1 방향 먼저. 왜? 그래야 2번 방향이
    d[i][0][0] = max(d[i - 1][0][0], d[i - 1][0][1], d[i - 1][0][2]) + a[i][0]
    for j in range(1, m):
        d[i][j][0] = max(d[i - 1][j][0], d[i - 1][j][1], d[i - 1][j][2]) + a[i][j]
        d[i][j][1] = max(d[i][j - 1][0], d[i][j - 1][1]) + a[i][j]
    for j in range(m - 2, -1, -1):
        d[i][j][2] = max(d[i][j + 1][0], d[i][j + 1][2]) + a[i][j]

print(max(d[n - 1][m - 1]))
