# 읽기 편한 코드
# 주석
# 확장 가능성

# flag_type 설정
def set_flag_type(flag_rules, flag):
    for rule in flag_rules:
        if flag == rule[0]:
            return rule[1]
    return "ERROR"


# flag_type에 대응하는 flag argument 인지 검사
def valid_argument(flag_type, argument):
    if flag_type == "STRING":
        if not argument.isalpha():
            return False
    elif flag_type == "NUMBER":
        if not argument.isdigit():
            return False
    return True


def solution(program, flag_rules, commands):
    # 인덱싱 하기 위해 flag_rules 리스트화
    flag_rules = [rule.split() for rule in flag_rules]
    answer = []

    """ 각 command에 대하여 타당성 검사 """
    for command in commands:
        # 리스트화
        command = command.split()
        # 리스트를 순회하기 위한 인덱스
        idx = 0
        # 프로그램 명이 일치하는가
        if command[idx] != program:
            answer.append(False)
            break

        """ flag role 에 부합하는지 확인하기 위해 리스트 순회 """
        # while문을 무사히 마치면 True, break로 탈출하면 False
        while idx + 1 < len(command):
            # 항상 flag로 시작하도록 구성
            idx += 1
            flag = command[idx]
            # flag는 '-'(dash)로 시작해야 한다.
            if flag[0] != '-':
                break
            # flag_type 설정
            flag_type = set_flag_type(flag_rules, flag)
            # flag_type 에러
            if flag_type == "ERROR":
                break
            """ flag_type에 대응하는 flag argument 인지 검사 """
            # NULL인 경우, 다음에 인자가 온다면 다음 flag 검사 시 검출됨
            if flag_type == "NULL":
                continue
            idx += 1
            # flag_type에 따른 인자가 아니라면 실패
            if not valid_argument(flag_type, command[idx]):
                break
        else:
            answer.append(True)
            continue
        answer.append(False)
    return answer


program = "line"
flag_roles = ["-s STRING", "-n NUMBER", "-e NULL"]
# flag_roles = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -n 100 -s hi -e", "lien -s Bye"]
# commands = ["line -s 123 -n HI", "line fun"]
print(solution(program, flag_roles, commands))
