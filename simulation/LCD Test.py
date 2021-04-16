"""
back: 크게 나눠라 - 작은 문제로 분류 / 공통점을 발견하라
deep: 큰 그림부터 그려. 노가다는 나중에. 노가다 했는데 방향이 틀렸으면?
"""
# 너무 복잡하다. 효율적으로 다시 짜보자
# 문자열을 왜 계속 더하냐.. 매번 새로 객체 만드는데.

# True, False 말고 0,1로 해도 똑같다. 0,1이 가독성 좋다.
num = [
    (True, True, False, True, True, True, True),  # 0
    (False, False, False, False, False, True, True),  # 1
    (True, False, True, True, True, True, False),  # 2
    (True, False, True, False, True, True, True),  # 3
    (False, True, True, False, False, True, True),  # 4
    (True, True, True, False, True, False, True),  # 5
    (True, True, True, True, True, False, True),  # 6
    (True, False, False, False, False, True, True),  # 7
    (True, True, True, True, True, True, True),  # 8
    (True, True, True, False, True, True, True),  # 9
]
l, n = map(int, input().split())
data = [int(c) for c in str(n)]

# 5개 라인으로 분할
for part in range(5):
    line = ""
    if part % 2 == 0:  # 가로 출력
        for x in data:
            temp = "-" if num[x][part] else " "
            line += " " + temp * l + "  "
        print(line)
    else:  # 세로 출력
        for x in data:
            line += "|" if (part == 1 and num[x][1]) or (part == 3 and num[x][3]) else " "
            line += " " * l
            line += "| " if (part == 1 and num[x][5]) or (part == 3 and num[x][6]) else "  "
        for _ in range(l):
            print(line)
