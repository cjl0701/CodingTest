# 소수의 연속합
n = int(input())


# n 미만의 소수를 모두 구한다.
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


prime = eratos(n)
l = r = ans = 0
sum = prime[0] if prime else 0
while l <= r < len(prime):
    if sum <= n:
        if sum == n:
            ans += 1
        r += 1
        if r < len(prime):
            sum += prime[r]
    else:
        sum -= prime[l]
        l += 1
        if len(prime) > l > r:
            r = l
            sum += prime[r]
print(ans)
