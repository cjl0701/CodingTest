# 정당성: 빼기 보다 나누기가 빠르다!
n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # 더 이상 나눌 수 없으면 탈출
    if n < k: break
    n //= k
    result += 1

result += (n - 1)
print(result)
