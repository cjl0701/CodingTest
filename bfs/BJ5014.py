from collections import deque

f, s, g, u, d = map(int, input().split())
dist = [-1] * (f + 1)  # d[i]:i에 오기위해 누른 버튼 수
q = deque()
q.append(s)
dist[s] = 0  # s==g or u,d==0일 경우 때문에 -1로 초기화 해야 한다. -1로 초기화하는 습관을 갖자.
while q:
    cur = q.popleft()
    for next in (cur + u, cur - d):
        if 1 <= next <= f:
            if dist[next] == -1:
                dist[next] = dist[cur] + 1
                q.append(next)
if dist[g] == -1:
    print("use the stairs")
else:
    print(dist[g])
