# pc 예약받아 가능한 큰 수익 내는 경우
# 최대합 => 모든 조합 생성 or dp
p, n, h = map(int, input().split())
pc = [[] for _ in range(p)]
for _ in range(n):
    com, hour = map(int, input().split())
    if hour < h:
        pc[com - 1].append(hour)

for i in range(p):
    ans = 0
    if pc[i]:  # 예약이 비지 않았다면
        # 모든 조합 만들어 최대 수익을 구한다.
        l = len(pc[i])
        for bm in range(1, 1 << l):
            cur = 0
            for idx in range(l):
                if bm & (1 << idx) > 0:
                    cur += pc[i][idx]
            if cur <= h:
                ans = max(ans, cur)
    print(i + 1, ans * 1000)
