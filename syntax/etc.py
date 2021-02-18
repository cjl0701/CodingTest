answer = 3
# 조건부 표현식
result = "Success" if 1 < answer < 4 else "Fail"
print(result)


# 여러 개의 반환 값을 가질 수 있다 - by 패킹, 언패킹
def operator(a, b):
    return a + b, a - b, a * b, a / b  # 패킹


a, b, c, d = operator(7, 3)  # 언패킹
print(a, b, c, d)  # 10 4 21 2.3333333333333335

