# BJ 12969
""" 왜 발상 못했나?
1. 수가 크면 dict 쓸 생각 밖에 못함
2. 문자열을 출력하라고 해서 문자열을 보존하고 있어야 하는 줄 알았다. 그래서 문자열을 붙일 생각을..
    => skill이 있다.

새로운 접근법
1. 이전 답을 활용하려면, 길이, a,b,c 갯수, 조건쌍 갯수를 알아야.. 정보가 너무 많다! 
 => 인자로 표현한다! d[][][][]의 답은 T/F
2. 문자열
 => 문자 단위로 접근.
3. 미래 지향적 점화식
 => 이전 답을 이용해서 현재 답을 구한다면, 반대로 d[i]=>d[i+k]도 가능
4. 가능한거 하나만 찾는다
 => a를 넣었을 때 가능? 안되면 b로 넣었을 때 가능?
 => dp와 bf의 콤비네이션. 가능해서 진행했던거면 또 해보지 않는다. 
5. 같은 상태인지 헷갈림
 => 할 수 있는 선택이 같으면 같은 상태
"""


# 재귀와 df의 콤비네이션
def f(l, a, b, p):
    if l == n:
        return True if p == k else False
    # d: 가능/불가능 여부. 가능해서 탐색했던 방법이면 더 진행 x
    if d[l][a][b][p]:  # 앞으로 할 수 있는 선택이 같으므로 같은 상태이다.
        return False
    d[l][a][b][p] = True  # 방문 처리
    global ans
    temp = ans
    # a,b,c를 각각 추가할 경우, 쭉 진행해본다.
    ans = temp + 'A'
    if f(l + 1, a + 1, b, p):
        return True
    ans = temp + 'B'
    if f(l + 1, a, b + 1, p + a):
        return True
    ans = temp + 'C'
    if f(l + 1, a, b, p + a + b):
        return True
    return False  # 다 탐색 해봤는데 안 됨


limit = int(30 * 29 / 2 + 1)  # 436
d = [[[[False] * limit for _ in range(31)] for _ in range(31)] for _ in range(31)]
n, k = map(int, input().split())
ans = ""
if f(0, 0, 0, 0):
    print(ans)
else:
    print(-1)
