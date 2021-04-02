# 프로그래머스
# sorted는 원본 변형x
def solution(array, commands):
    # commands 리스트의 각 원소에 람다식 매핑
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
