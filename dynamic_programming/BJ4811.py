# 알약
# DP는 같은 상황인지 다른 상황인지 구별하는게 중요하다
# => 같은 선택을 할 수 있다면 같은 상태

# 답: 서로 다른 문자열의 갯수 => 약을 먹는 방법의 수
# d[][]가 중복될 수 있으나, 앞 선택이 다르면 다른 조합이다!
d = [[-1] * 31 for _ in range(31)]  # d[f][h]: 약이 f개, 반 조각이 h개 있을 때, 약을 먹는 방법 수
"""bottom-up
d[0][0] = 1
for f in range(31):
    for h in range(31):
        if d[f][h] == 0:
            if f - 1 >= 0:  # 한 알 짜리 꺼낼 경우
                d[f][h] += d[f - 1][h + 1]
            if h - 1 >= 0:  # 반 알 짜리 꺼낼 경우
                d[f][h] += d[f][h - 1]
"""


def func(f, h):
    if f == 0:
        return 1
    if d[f][h] == -1:
        if h == 0:
            d[f][h] = func(f - 1, h + 1)
        else:
            d[f][h] = func(f - 1, h + 1) + func(f, h - 1)
    return d[f][h]


while True:
    n = int(input())
    if n == 0:
        break
    print(func(n, 0))

"""
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
"""
