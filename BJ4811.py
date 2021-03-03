# 알약
# 올바른 괄호랑 비슷한데?
d = [0] * 61  # d[i]: 길이가 i일때 올바른 조합의 갯수
d[0] = 1
for i in range(2, 61, 2):  # 짝수만 나온다
    for k in range(2, i + 1, 2):
        d[i] += d[k - 2] * d[i - k]
while True:
    n = int(input())
    if n == 0: break
    print(d[2*n])
