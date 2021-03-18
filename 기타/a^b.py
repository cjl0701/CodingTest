a, b = 10, 3
# O(b)
ans = 1
for _ in range(b):
    ans *= a
print(ans)


# O(logb) 분할정복을 이용한 방법
# b가 짝수일 때, 홀수일 때 다르게 나뉨.
def calc(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        temp = calc(a, b // 2)
        return temp * temp
    else:
        return a * calc(a, b - 1)


print(calc(3.141592, 3))

# 이진수를 이용한 방법. 2씩 나눠가므로 O(logb)
# a^27. 27 => 11011 => 2^4*2^3.. a^x들의 곱으로.
ans = 1
while b > 0:
    if (b & 1) == 1:
        ans *= a
    b >>= 1
    a = a * a  # a, a^2, a^4, a^8
print(ans)
