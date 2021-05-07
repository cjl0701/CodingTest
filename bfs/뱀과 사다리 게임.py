# https://www.acmicpc.net/problem/16928
"""
1. 어떤 예외 사항이 있는지 모르니 좀 더 포용적으로 구성하자
2. bfs를 이용하면 밟은 곳 또 안 밟는다. 최악의 경우 모든 칸. 충분히 효과적이다.
"""
from collections import deque

n, m = map(int, input().split())
move = [i for i in range(101)]
for _ in range(n + m):
    frm, to = map(int, input().split())
    move[frm] = to

d = [-1] * 101
d[1] = 0
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for k in range(1, 7):
        next = cur + k
        if next > 100: # 뱀 밟은 경우 continue하면 틀린다. 어떤 예외인지는 모르겠다.
            continue
        next = move[next]
        if d[next] == -1:
            d[next] = d[cur] + 1
            q.append(next)
print(d[100])
