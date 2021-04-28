# BJ 3019
# 구현하게 쉽게 기능을 분할해라
# 높이 차가 맞아야 한다.

def calc(i, s):
    if i + len(s) > c:
        return 0
    base = a[i] - (ord(s[0]) - ord('0'))
    for j in range(len(s)):
        if base != a[i + j] - (ord(s[j]) - ord('0')):
            return 0
    return 1


c, p = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
# 모든 자리에 놓아본다.
for i in range(c):
    # case별 문자열로 표현하는 스킬
    if p == 1:
        ans += calc(i, "0") + calc(i, "0000")  # 바닥만 문자열로 간단하게!
    elif p == 2:
        ans += calc(i, "00")
    elif p == 3:
        ans += calc(i, "001") + calc(i, "10")
    elif p == 4:
        ans += calc(i, "100") + calc(i, "01")
    elif p == 5:
        ans += calc(i, "000") + calc(i, "01") + calc(i, "101") + calc(i, "10")
    elif p == 6:
        ans += calc(i, "000") + calc(i, "00") + calc(i, "011") + calc(i, "20")
    elif p == 7:
        ans += calc(i, "000") + calc(i, "00") + calc(i, "110") + calc(i, "02")
print(ans)
""" 이건 실수할 가능성이 높다.
tet = [
    [],
    [(1, 1, 1, 1)],  # 예외처리: l 인경우는 무조건 성공
    [(1, 1)],
    [(1, 1, 2), (2, 1)],
    [(2, 1, 1), (1, 2)],
    [(1, 1, 1), (1, 2), (2, 1, 2), (2, 1)],
    [(1, 1, 1), (1, 1), (1, 2, 2), (3, 1)],
    [(1, 1, 1), (1, 3), (2, 2, 1), (1, 1)]
]

# 모든 자리에 놓아본다.
for idx in range(c - 1):
    # 각 케이스별로 가능한지 체크
    for case in tet[p]:
        length = len(case)
        if idx + length > c:  # 범위 넘어감
            continue
        # 높이 차가 맞아야 한다.
        for i in range(length - 1):
            if case[i] - case[i + 1] != a[idx + i] - a[idx + i + 1]:
                break
        else:
            ans += 1

if p == 1:
    ans += c
"""
