# 읽기 편한 코드
# 주석
# 확장 가능성


# flag_type에 대응하는 flag argument 인지 검사
from collections import defaultdict

# 타당한 인자가 뒤따르는지 검사. 다음 인자 반환
def check_arguments(flag_type, command, idx, flag_rules_dict):
    # NULL인 경우 인자가 없다
    if flag_type == "NULL":
        return idx
    elif flag_type == "STRING":
        return idx + 1 if command[idx].isalpha() else -1  # '-'가 들어가도 False
    elif flag_type == "NUMBER":
        return idx + 1 if command[idx].isdigit() else -1

    """ 여러 인자를 확인해야 하는 경우, flag를 만날 때까지 진행"""
    # 타당 여부 기록
    ok = False
    if flag_type == "STRINGS":
        # ERROR 라는 건 flag가 아니라는 것
        while flag_rules_dict[command[idx]] == "ERROR":
            if command[idx].isalpha():
                ok = True
                idx += 1
            else:
                return -1
    elif flag_type == "NUMBERS":
        while flag_rules_dict[command[idx]] == "ERROR":
            if command[idx].isdigit():
                ok = True
                idx += 1
            else:
                return -1
    # 타당하지 않은 경우라면 -1 반환
    return idx if ok else -1


def solution(program, flag_rules, commands):
    # 빠른 접근을 위해 dictionary 화
    flag_rules_dict = defaultdict(lambda: "ERROR")
    for rule in flag_rules:
        flag, type = rule.split()
        flag_rules_dict[flag] = type
    answer = []

    """ 각 command에 대하여 타당성 검사 """
    for command in commands:
        # 리스트화
        command = command.split()
        # 프로그램 명이 일치하는가
        if command[0] != program:
            answer.append(False)
            break
        idx = 1  # command 리스트를 순회하기 위한 인덱스
        """ flag role 에 부합하는지 확인하기 위해 리스트 순회 """
        # while문을 무사히 마치면 True, break로 탈출하면 False
        while idx < len(command):
            # 항상 flag로 시작하도록 구성
            flag = command[idx]
            flag_type = flag_rules_dict[flag]
            # rule에 속하지 않는 flag라면 False
            if flag_type == "ERROR":
                break
            """ flag_type에 대응하는 flag argument 인지 검사 """
            idx = check_arguments(flag_type, command, idx + 1, flag_rules_dict)
            # flag_type에 대응하는 인자가 아니라면 실패
            if idx == -1:
                break
        else:
            answer.append(True)
            continue
        answer.append(False)
    return answer


# program = "line"
# flag_roles = ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]
# flag_roles = ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -s 123 -n HI", "line fun"]
# flag_roles = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
# commands=["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]
program = "trip"
flag_roles = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]

print(solution(program, flag_roles, commands))
