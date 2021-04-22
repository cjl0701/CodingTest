a = 1e9  # 1억
print(int(a))
pi = 314e-2
print(pi)

# 실수는 오차를 포함한다. 이진수는 실수를 정확히 표현할 수 없다.
a = .3 + .6
print(a)  # 0.8999999999999999
# => round로 반올림
print(round(a, 1))  # 0.9
print(round(3.1423, 2))  # 3.14
