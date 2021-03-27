# 같은 수를 2번 이상 연속x -> 어떤 수로 끝나는 지 표시
# 틀리는 이유: 논리 부실 or 구현 실수 or 예외 처리
MOD = 1000000009
d = [[0] * 4 for _ in range(100001)]  # d[i][j] 끝이 j로 끝나고 i를 만드는 방법 수
# 답이 틀림 -> 직접 과정을 찍어본다.
for i in range(1, 100001):
    if i - 1 >= 0:
        d[i][1] = d[i - 1][2] + d[i - 1][3]
        if i == 1:  # 예외처리
            d[i][1] = 1
    if i - 2 >= 0:
        d[i][2] = d[i - 2][1] + d[i - 2][3]
        if i == 2:
            d[i][2] = 1
    if i - 3 >= 0:
        d[i][3] = d[i - 3][1] + d[i - 3][2]
        if i == 3:
            d[i][3] = 1
    d[i][1] %= MOD
    d[i][2] %= MOD
    d[i][3] %= MOD
    # 코드가 길기만 하고 추상적이라 헷갈림.. 3개 정도면 직관적으로
    # for end in range(1, 4):
    #     if i - end == 0:
    #         d[i][end] = 1  # i==end 일 때 자기 자신을 쓰는 방법은 한가지
    #     elif i - end > 0:
    #         if end == 1:
    #             d[i][end] += d[i - end][2] + d[i - end][3]
    #         elif end == 2:
    #             d[i][end] += d[i - end][1] + d[i - end][3]
    #         elif end == 3:
    #             d[i][end] += d[i - end][1] + d[i - end][2]
    #     d[i][end] %= MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % MOD)
