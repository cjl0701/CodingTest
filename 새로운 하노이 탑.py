from collections import deque

start = []
for _ in range(3):
    temp = input()
    if temp == "0":
        start.append("")
    else:
        start.append(temp.split()[1])
start = tuple(start)
cnt = [0, 0, 0]
for s in start:  # ''은 무시
    for ch in s:
        cnt[ord(ch) - ord('A')] += 1

q = deque()
q.append(start)
# d = defaultdict(lambda: -1)
d = dict()
d[start] = 0

while q:
    now = q.popleft()
    # 이동
    for frm in range(3):
        for to in range(3):
            if now[frm] == "" or frm == to:
                continue
            next = list(now)
            next[to] += now[frm][-1]
            next[frm] = now[frm][:-1]
            next = tuple(next)
            if next not in d:  # defualtdict이 아닌 그냥 dict인 경우
                d[next] = d[now] + 1
                q.append(next)

# 체크 과정이 길다면, 매번 체크하는 것보다 bfs 쭉 진행하는게 낫다
ans = ["", "", ""]
for i, x in enumerate(cnt):
    ans[i] = chr(ord("A") + i) * x
print(d[tuple(ans)])
