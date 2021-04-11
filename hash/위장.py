from collections import Counter
from functools import reduce


def solution(clothes):
    counter = Counter(map(lambda l: l[1], clothes))
    # ans = 1
    # for c in counter.items():
    #     ans *= (c[1] + 1)
    # return ans - 1
    return reduce(lambda x, y: x * (y + 1), counter.values(), 1) - 1
