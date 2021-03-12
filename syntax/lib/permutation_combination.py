data = ['A', 'B', 'C']

# 순열
from itertools import permutations

print(permutations(data, 3))  # <itertools.permutations object at 0x000001F94FB6E8B0>
# 리스트 안 만들어도 iterable이라 for문에 바로 쓸 수 있다.
result = list(permutations(data, 3))  # 3개 골라 순서 있게 나열
print(result)  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'),,,
result = list(permutations(data, 2))  # 2개 골라 순서 있게 나열
# (1,7), (1,9), (1,9) 이런식으로 같은 것을 걸러주진 않는다.next_permutation 이나 재귀 or set

# 조합
from itertools import combinations

result = list(combinations(data, 2))  # 2개 뽑는 모든 조합 구하기
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열
from itertools import product

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 (중복 허용)
print(result)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),,,,

# 중복 조합
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 (중복 허용)
print(result)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
