# BJ 1629
def calc(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        memo = calc(a, b // 2)  # 절반씩 줄이므로 O(logN)
        return (memo * memo) % c
    else:
        return (a * calc(a, b - 1)) % c  # 짝수가 된다

a, b, c = map(int, input().split())
print(calc(a, b))
