# 퇴사 2
# 깔끔하게 n-1 안 쓰는 방법으로 개선 => d[i]=~ 가 아니라 d[i]=>d[i+x]

n = int(input())
temp = [list(map(int, input().split())) for _ in range(n)]
t, p = map(list, zip(*temp))
d = [0] * (n + 50)  # d[i]: i+1일째 받을 수 있는 최대 금액
for i in range(n):
    # 상담
    d[i + t[i]] = max(d[i + t[i]], d[i] + p[i])  # 덮어 쓰일 수 있으니 max
    # 상담 x
    d[i + 1] = max(d[i + 1], d[i])

print(d[n])
