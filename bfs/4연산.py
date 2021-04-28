# https://www.acmicpc.net/problem/14395
from collections import deque

operator = ('*', '+', '-', '/')
s, goal = map(int, input().split())
if s == goal:
    print(0)
    exit(0)
d = dict()
d[s] = (-1, -1)
q = deque()
q.append(s)
ans = ""
while q:
    now = q.popleft()
    if now == goal:
        while d[now][0] != -1:
            ans = operator[d[now][1]] + ans
            now = d[now][0]
        break
    for i, next in enumerate((now ** 2, 2 * now, 0, 1)):
        if not (1 <= next <= 10 ** 9) or next in d:
            continue
        d[next] = (now, i)
        q.append(next)
print(ans if ans else -1)
