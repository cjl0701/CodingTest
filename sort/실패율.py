# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
# 실패율을 구한다. 배열에 넣고 정렬


def solution(N, stages):
    length = len(stages)
    answer = []
    for i in range(1, N + 1):
        count = stages.count(i)  # counter 안 만들어도 된다!
        if length == 0:
            answer.append((i, 0))
        else:
            answer.append((i, count / length))
        length -= count

    answer.sort(key=lambda tp: (-tp[1], tp[0]))
    answer = [tp[0] for tp in answer]  # 새로운 리스트를 만들고 answer로 가리킨다.
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4, 4, 4, 4, 4]

N = 4
stages = [1, 1, 1, 1]

print(solution(N, stages))
