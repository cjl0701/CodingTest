# 1,2,3 더하기 4 https://www.acmicpc.net/problem/15989
limit = 10000
d = [0] * (limit + 1)
d[0] = 1
# 1로 끝나는 것, 2로 끝나는 것 이렇게 순서대로 구하면 중복이 생기지 않는다.
for end in range(1, 4):
    for i in range(1, limit + 1):
        if i - end >= 0:
            d[i] += d[i - end]
t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
