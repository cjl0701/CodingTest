# https://www.acmicpc.net/problem/3687
# 완전탐색(및 dfs,bfs)하기 전에 시간 복잡도 반드시 구하기
# 시간복잡도 먼저 생각했으면 DP 찾았다..
# DP 규칙이 안보이면 손으로 많이 풀어봐라
LIMIT = int('1' * 50)
num = (0, 0, 1, 7, 4, 2, 0, 8, 10)
d = [0 for _ in range(101)]  # i개로 만들수 있는 최소값
# 초기값
for i in range(2, 9):
    d[i] = num[i]
d[6] = 6  # 예외 때문에 따로 기록

for i in range(9, 101):  # i-j가 0,1이 되면 안됨
    for j in range(2, 8):  # 0개, 1개로 만들 수는 없다 / 8부터는 자릿수가 바뀐다.
        temp = d[i - j] * 10 + num[j]
        if d[i] == 0 or d[i] > temp:
            d[i] = temp

tc = int(input())
while tc > 0:
    tc -= 1
    n = int(input())
    print(d[n], end=" ")
    max_ans = ""
    while n != 0:
        if n == 3:
            max_ans = "7" + max_ans
            n -= 3
        else:
            max_ans = "1" + max_ans
            n -= 2
    print(max_ans)
