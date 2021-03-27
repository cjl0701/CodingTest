# n은 1,000,000이므로 d[] 크기를 백만으로 만드는 건 에바..가 아니라 해도 되는구나..
# d의 크기가 백만이어도 시간, 공간 상 괜찮다.
MOD = 1000000009
t = int(input())
d = [0] * 1000001  # d[i]: i를 1,2,3으로 나타내는 방법 수
d[0] = 1
for i in range(1, 1000001):
    for num in range(1, 4):
        if i - num >= 0:
            d[i] += d[i - num]  # d[i-1](1), d[i-2](2), d[i-3](3)
        d[i] %= MOD
for _ in range(t):
    n = int(input())
    print(d[n])
