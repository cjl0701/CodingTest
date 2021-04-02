# 문자열 비교: O(l) 너무 길다 => 해시값으로 비교하면 O(1)
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


participant = ['a', 'a', 'a', 'b', 'c']
completion = ['a', 'b', 'c', 'd']
Counter(participant) - Counter(completion)  # => Counter({'a': 1}). 갯수도 빼준다.
print(solution(participant, completion))
