# 치킨 배달
# 순서가 중요하지 않은 조합이라면 start로 건너 뛰기!
"""시간 초과..
시간 초과가 나면 전체 횟수 살피기 => 건너 뛸 수 있나보기
1. 아니 애초에 왜 bfs를 했지?? 미친.. 습관이 이렇게 무섭다.
2. 시간 계산 했는데.. => 구현해보니 내부 계산이 많아져 초과함..
3. 코드를 짧게 하려다 순열로 풀었다..
"""

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = list()
chicken = list()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))


def go(select, chi, start):
    if select == m:
        # 치킨거리 합을 구한다.
        s = 0
        for h in house:
            dist = []
            for c in chi:
                dist.append(abs(h[0] - c[0]) + abs(h[1] - c[1]))
            s += min(dist)
        global ans
        ans = min(ans, s)
        return
    """
    시간 초과 난 이유: 코드를 줄이려고 하다보니 조합이 아닌 순열로 뽑게 됐다..
    for c in chicken: 최악 13!
        go(select + 1, chi + [c])
    """
    for i in range(start, len(chicken)):
        go(select + 1, chi + [chicken[i]], i + 1)


ans = 100000
go(0, [], 0)
print(ans)
