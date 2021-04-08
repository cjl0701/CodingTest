from collections import defaultdict


def solution(inp_str):
    check = [False, False, False, False, False]
    word = defaultdict(lambda: 0)  # default 값을 0으로 설정
    type = [False, False, False, False]  # 문자 타입 (대,소,숫,특)
    prev = ""  # 이전 문자
    cnt = 0  # 연속
    # 1. 길이 검사
    if not 8 <= len(inp_str) <= 15:
        check[0] = True
    # 문자 하나하나 조사
    for w in inp_str:
        # 2. 타입 조사
        ord_w = ord(w)
        if ord('A') <= ord_w <= ord('Z'):
            type[0] = True
        elif ord('a') <= ord_w <= ord('z'):
            type[1] = True
        elif ord('0') <= ord_w <= ord('9'):
            type[2] = True
        elif w in "~!@#$%^&*":
            type[3] = True
        else:
            check[1] = True
        # 4. 연속성 조사
        if prev == w:
            cnt += 1
            if cnt >= 4:
                check[3] = True
        else:
            prev = w
            cnt = 1
        # 문자 갯수 세기
        word[w] += 1

    # 3. 종류 조사
    t = 0
    for ty in type:
        if ty:
            t += 1
    if t < 3:
        check[2] = True
    # 5. 중복 문자 조사
    for w, l in word.items():
        if l >= 5:
            check[4] = True
            break
    answer = [i + 1 for i in range(5) if check[i]]
    return answer if answer else [0]


inp_str = "??!!??"
print(solution(inp_str))
"""
"AaTa+!12-3"
"aaaaZZZZ)"
"CaCbCgCdC888834A"
"ZzZz9Z824"
"""
