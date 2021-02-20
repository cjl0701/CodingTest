data = ['A', 'B', 'C']

# 순열
from itertools import permutations

result = list(permutations(data, 3))  # 3개 골라 순서 있게 나열
print(result)  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'),,,
result = list(permutations(data, 2))  # 2개 골라 순서 있게 나열

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
