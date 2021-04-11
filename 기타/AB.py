# https://www.acmicpc.net/problem/12970
# 아이디어, 중요한 기본 스킬
"""
skill. 최대 a*b까지 => a*b인 경우가 항상 존재.
 b,b-1,b-2,,,로 1씩 차이나므로 0~a*b사이 모든 수를 만들 수 있다
"""
"""
틀린 이유: a 범위가 넘어서 b개 고르려면 조합 수가 너무 많다.
=> 관점을 바꿔, 0~b 사이의 수를 a번 선택하는 것으로 보자.
=> 1씩 차이나므로 모든 수를 만들 수 있다. -> 큰 수부터 선택하는 게 유리
=> cnt 배열에 갯수를 하나씩 추가!  
"""

n, k = map(int, input().split())
for b in range(n + 1):  # n 포함이니 n+1
    a = n - b
    if a * b < k:
        continue
    """0~b까지 a번 선택해 합을 k로 만드는 법: 1씩 차이나므로 다 됨. 큰 수부터 선택!"""
    cnt = [0] * (b + 1)  # 인덱스는 순서가 아닌 더 해야 하는 값
    for _ in range(a):  # a번 선택해야 한다.
        x = min(b, k)  # 큰 수부터 선택하는 게 최선!
        cnt[x] += 1
        k -= x

    # 출력: 문자열 매번 합치는 것보다 하나씩 출력하는게 빠르네..
    for i in range(b, -1, -1):
        print("A" * cnt[i], end="")
        if i > 0:
            print("B", end="")
    exit(0)
print(-1)
""" 
# 정해. 완탐 O(2^N)
def go(i, a, cnt):
    if i == n:
        return cnt == k
    if not check[i][a][cnt]:
        check[i][a][cnt] = True

        global ans
        temp = ans
        # A 추가
        ans = temp + 'A'
        if go(i + 1, a + 1, cnt):
            return True
        # B 추가
        ans = temp + 'B'
        if go(i + 1, a, cnt + a):
            return True
    return False


n, k = map(int, input().split())
check = [[[False] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)] for _ in range(n + 1)]
ans = ""
print(ans if go(0, 0, 0) else -1)
"""
