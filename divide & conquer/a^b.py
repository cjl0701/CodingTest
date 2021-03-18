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