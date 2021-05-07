# https://www.acmicpc.net/problem/16235
""" 시간 초과 난 이유 = 비효율적 코딩
1. dict를 써서 매회 if-else 반복 => defaultdict
2. 새로운 리스트로 갈아주는데 굳이 pop()해서 지울 필요 x,
3. 매번 튜플을 만들어서 dict 조회 => i,j<10이니 이 경우엔 튜플 생성 비용이 더 큼
4. 양분 주려면 어차피 i,j 전부 순회해야 하는데 굳이 튜플 만들어서 dict 사용 => 전체 연산 과정을 생각했어야
"""
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
n, m, k = map(int, input().split())
land = [[5] * n for _ in range(n)]
nutr = [list(map(int, input().split())) for _ in range(n)]
trees = [[list() for _ in range(n)] for _ in range(n)]  # [[list()]*n for _ in range(n)] 같은 리스트 n개 복사..
for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

# 편의대로 순서 바꿔도 된다
for _ in range(k):
    next = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dead = 0
            survived = []
            trees[i][j].sort()
            for tree in trees[i][j]:
                if tree <= land[i][j]:
                    land[i][j] -= tree
                    survived.append(tree + 1)
                    if (tree + 1) % 5 == 0: # 즉시 나이를 먹는다했으니
                        for dir in range(8): # 가을
                            ni, nj = i + dx[dir], j + dy[dir]
                            if 0 <= ni < n and 0 <= nj < n:
                                next[ni][nj] += 1
                else:
                    dead += tree // 2
            trees[i][j] = survived
            land[i][j] += nutr[i][j] + dead # 여름, 겨울 동시 진행
    for i in range(n):
        for j in range(n):
            for _ in range(next[i][j]): 
                trees[i][j].append(1)

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)
