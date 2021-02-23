# N개 중 M개 고른 수열 (같은 것을 포함한 순열)
# permutations는 같은 것을 걸러줄까? 안 걸러준다
# (1,7), (1,9), (1,9) 이런식..
# set에 담갔다 빼야한다.
import sys
from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))

# for p in sorted(list(set(permutations(data, m)))):
#     sys.stdout.write(' '.join(map(str, p)) + "\n")

