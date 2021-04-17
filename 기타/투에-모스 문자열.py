"""
직접구하면 시간 초과 (k<10^18)
어차피 0,1 반복 -> 인덱스 놀음 => 규칙 찾자!
"""
# k = int(input())
# x, _x = "0", "1"  # 첫번째
# for i in range(2, k + 1):
#     temp = x
#     x += _x
#     _x += temp
# print(x[k - 1])

""" 0<->1 바꾸는 법: ~ or 1-x """


def f(x, diff):
    # base case
    if x - diff == 0:
        return 0
    elif x - diff == 1:
        return 1

    # 규칙에 따라 이동
    if x // 2 - diff >= 0:
        return 1 - f(x // 2, diff)
    else:  # x//2보다 diff가 클 경우, diff도 조정
        return f(x // 2, diff - x // 2)


k = int(input()) - 1
# 규칙: 2^n-i 는 2^(n//2)-i 를 뒤집은 것.
limit = 1
while k > limit:
    limit *= 2
print(f(limit, limit - k))
