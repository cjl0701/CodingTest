# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3#
from functools import cmp_to_key

""" 약속 : 반환 값이 양수면 앞놈을 뒤로 보낸다 
* 정렬했을 때 a가 b보다 더 뒤에 있어야 한다면 0보다 큰 수를 반환해야 한다
* 정렬했을 때 a가 b보다 더 앞에 있어야 한다면 0보다 작은 수를 반환해야 한다
* 정렬했을 때 a와 b가 동등하다면 0을 반환해야 한다.
"""


def compare(x, y):
    return int(y + x) - int(x + y)


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(numbers)))


print(solution([0, 0, 100]))
