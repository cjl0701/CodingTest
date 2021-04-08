from math import gcd
"""최소 공배수 문제"""
s = input()
t = input()
"""방법 1: 실제로 문자열을 붙인다"""
S, T = s, t
while len(S) != len(T):  # 최소 공배수까지
    if len(S) < len(T):
        S += s
    else:
        T += t
print(1 if S == T else 0)

"""방법 2: 실제로 문자열을 붙이진 않고 인덱스 놀음"""
# 길이가 최대 50이므로, 최대 공배수는 최대 2500
# 2500까지 확장-> 오래걸리고 어차피 반복이니까 idx 놀음
# l1, l2 = len(s), len(t)
# for i in range(2500):
#     if s[i % l1] != t[i % l2]:
#         print(0)
#         exit(0)
# print(1)

"""방법 3: 최소 공배수 구해서 실제로 문자열을 붙인다"""
# g = gcd(l1, l2)
# a, b = l1 // g, l2 // g
# s1, s2 = "", ""
# for _ in range(b):
#     s1 += s
# for _ in range(a):
#     s2 += t
# print(1 if hash(s1) == hash(s2) else 0)
