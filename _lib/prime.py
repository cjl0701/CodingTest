# 소수: 약수가 1과 자기 자신 밖에 없는 수
# 2,3,5,7,11,13,,

# 소수인지 판별 O(√N)
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


print(is_prime(17))

# 에라토스테네스의 체: n 까지의 모든 소수 구하기  O(N*loglogN)
""" 소수의 배수는 소수가 아니다!
    1. 2~n까지 모든 수를 써 놓는다.
    2. 아직 지워지지 않은 수 중에서 가장 작은 수를 찾는다.(그 수는 소수이다)
    3. 그 수의 배수를 모두 지운다.
"""


def eratos(n):
    check = [False] * (n + 1)  # n개 리스트 초기화
    check[0] = check[1] = True  # [True, True, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(2, n + 1):
        if not check[i]:  # 소수라면 배수를 모두 지운다
            j = i * i  # i-1까지의 배수를 모두 지웠으므로 (i-1)*i 까지는 이미 처리됨
            while j <= n:
                check[j] = True
                j += i

    # 소수 리스트 전달, 필요에 따라 check를 반환해도 된다.
    l = []
    for i in range(n + 1):
        if not check[i]:
            l.append(i)
    return l


m, n = map(int, input().split())
for x in eratos(n):
    if x >= m: print(x)
print(eratos(11))  # [2, 3, 5, 7, 11]
