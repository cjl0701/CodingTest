# 종이 조각 https://www.acmicpc.net/problem/14391
# 각각 셀에 가로 혹은 세로 맵핑
# 이를 모든 경우에 대하여 진행
# 0,1 맵핑 => 비트마스크
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]  # '123' -> [1,2,3]
ans = 0
# 0000..0 ~ 1111..1
for s in range(1 << (n * m)):
    sum = 0
    # 가로 0
    for i in range(n):
        line = 0
        for j in range(m):
            if (s & 1 << (m * i + j)) == 0:
                line = line * 10 + arr[i][j]
            else:  # 세로를 만나면
                sum += line
                line = 0
        sum += line
    # 세로 1
    for j in range(m):
        line = 0
        for i in range(n):
            if (s & 1 << (m * i + j)) != 0:  # 자주 하는 실수 2가지
                line = line * 10 + arr[i][j]
            else:  # 가로를 만나면
                sum += line
                line = 0
        sum += line
    ans = max(ans, sum)

print(ans)
