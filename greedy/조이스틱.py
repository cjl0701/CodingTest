# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
# 문제 잘 읽자.. 2개나 놓쳤다.
# 정당성: 현재 할 수 있는 선택이 왼쪽 or 오른쪽 밖에 없다. 매번 짧은 쪽은 선택하는 것이 최선이다.
def solution(name):
    n = len(name)
    move = 0
    left = n # 남은 갯수
    ok = [False] * n
    for i in range(n):
        if name[i] == 'A':
            ok[i] = True
            left -= 1

    idx = 0
    while left:
        diff = 0
        while True:
            # 오른쪽 이동(오른쪽 우선)
            if not ok[idx + diff]:
                idx += diff
                break
            # 왼쪽 이동
            elif not ok[(idx - diff + n) % n]:
                idx -= diff
                break
            diff += 1
        ok[idx] = True
        left -= 1
        move += diff + min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)

    return move
