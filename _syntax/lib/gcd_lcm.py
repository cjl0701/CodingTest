import math

# 최대 공약수(GCD)
math.gcd(21, 14)  # 7


# 유클리드 호제법으로 직접 구하기
def uclid(a, b):
    if a % b == 0:
        return b
    else:
        return uclid(b, a % b)

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)


lcm(21, 14)  # 42
