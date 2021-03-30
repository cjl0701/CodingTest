# BJ 3568
# 구분자를 기준으로 나눈다
strings = []
now = ""
for c in input():
    if c in ' ,;':
        if now:
            strings.append(now)
            now = ""
    else:
        now += c
# 뒤집기
base = strings[0]
for i in range(1, len(strings)):
    s = base
    slist = list(strings[i])
    while slist and not 'a' <= slist[-1] <= 'z':
        if slist[-1] == '[':
            s += ']'
        elif slist[-1] == ']':
            s += '['
        else:
            s += slist[-1]
        slist.pop()
    print(s + " " + "".join(slist) + ";")
# string = input().split()
# for i in range(1, len(string)):
#     type = []
#     var = ""
#     for c in string[i][:-1]:
#         if c.isalpha():
#             var = var + c
#         else:
#             if c == '[':
#                 c = "[]"
#             if c == ']':
#                 continue
#             type.append(c)
#     type.reverse()
#     print(string[0] + ''.join(type) + " " + var + ";")
