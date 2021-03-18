# BJ 1629
"""분할정복
def calc(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        memo = calc(a, b // 2)  # 절반씩 줄이므로 O(logN)
        return (memo * memo) % c
    else:
        return (a * calc(a, b - 1)) % c  # 짝수가 된다
"""

a, b, c = map(int, input().split())
# 이진수 활용
# a^b = a^1*a^2*a^8*a^16 (b=11011)
ans = 1
while b > 0:
    if (b & 1) == 1:
        ans = (ans * a) % c
    a = (a ** 2) % c
    b >>= 1
print(ans)
