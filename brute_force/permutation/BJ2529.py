# 부등호 https://www.acmicpc.net/problem/2529

# k+1 자리 숫자 모든 순열
# 최소: 오름차순일 때 가장 먼저 성립
# 최대: 내림차순일 때 가장 먼저 성립
from itertools import permutations

k = int(input())
operators = input().split()
permutation = list(permutations(range(0, 10), k + 1))


def valid(arr, operators):
    for i in range(len(operators)):
        if operators[i] == '<' and arr[i] >= arr[i + 1]:
            return False
        if operators[i] == '>' and arr[i] <= arr[i + 1]:
            return False
    return True


big, small = [], []
for p in permutation:
    if valid(p, operators):
        small = p
        break

permutation.sort(reverse=True)

for p in permutation:
    if valid(p, operators):
        big = p
        break

# 리스트->문자열 : join!
print(''.join(map(str, big)))
print(''.join(map(str, small)))
