t = int(input())
d = [0] * 11  # d[i]: i를 1,2,3으로 나타내는 방법 수
d[0] = 1
for i in range(1, 11):
    for num in range(1, 4):
        if i - num >= 0:
            d[i] += d[i - num]  # d[i-1](1), d[i-2](2), d[i-3](3)

for _ in range(t):
    n = int(input())
    print(d[n])
