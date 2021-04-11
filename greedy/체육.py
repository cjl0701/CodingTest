# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
# 정당성: 앞놈한테 먼저 빌려야 뒷사람 선택지가 2개가 된다!
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1) # 원소 지우기
        elif r + 1 in _lost:
            _lost.remove(r + 1)

    return n - len(_lost)
