n, m = map(int, input().split())
# 단순한 완전 탐색이면 중첩 for문
bad_combi = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    bad_combi[a][b] = bad_combi[b][a] = True

ans = 0
for a in range(1, n - 1):
    for b in range(a + 1, n):
        for c in range(b + 1, n + 1):
            if not (bad_combi[a][b] or bad_combi[a][c] or bad_combi[b][c]):
                ans += 1
print(ans)

"""
def go(cnt, start, a):
    if cnt == 3:
        if bad_combi[a[0]][a[1]] or bad_combi[a[0]][a[2]] or bad_combi[a[1]][a[2]]:
            return 0
        return 1

    ans = 0
    for i in range(start, n + 1):
        a.append(i)
        ans += go(cnt + 1, i + 1, a)
        a.pop()
    return ans


print(go(0, 1, []))
"""
# 백트래킹이라고 항상 빠른건 아니다. 체크 과정이 길다.
"""
def go(cnt, start, graph, possible):
    if cnt == 3:
        return 1
    ans = 0
    for i in range(start, n + 1):
        if possible[i]:
            # 선택 -> 불가능
            memo = []
            for e in graph[i]:  # 자신 포함
                if possible[e]:
                    memo.append(e)
                    possible[e] = False
            ans += go(cnt + 1, i + 1, graph, possible)
            # 선택 취소 -> 가능
            for e in memo:
                possible[e] = True
    return ans
"""
