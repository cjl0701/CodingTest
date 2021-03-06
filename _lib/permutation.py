# 첫 순열: 오름차순 / 마지막 순열: 내림차순
# 다음 순열: 마지막->처음
def next_permutaion(a):
    i = len(a) - 1
    # 마지막 부분 순열의 경계 찾기(앞으로 이동하며 내림차순의 끝)
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:  # 전부 내림차순: 최후 순열
        return False
    # 경계 swap: 마지막 부분 순열을 첫 부분 순열로 바꾸는 과정
    j = len(a) - 1
    while a[j] <= a[i - 1]:  # 앞 놈(a[i-1])보다 다음으로 큰 수를 찾아 swap
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    # 첫 부분 순열 만들기(경계 이후를 오름차순으로 바꾼다)
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


# 이전 순열
def prev_permutaion(a):
    i = len(a) - 1
    # 마지막 부분 순열의 경계 찾기(앞으로 이동하며 오름차순의 끝)
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i <= 0:  # 전부 오름차순: 최초 순열
        return False
    # 경계 swap: 첫 순열을 마지막 순열로 바꾸는 과정
    j = len(a) - 1
    while a[j] >= a[i - 1]:  # 앞 놈(a[i-1])보다 다음으로 작은 수를 찾아 swap
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    # 마지막 순열 만들기(경계 이후를 내림차순으로 바꾼다)
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


# 사용 예
n = 5
l = [1, 2, 3, 4, 5]
if prev_permutaion(l):
    print(' '.join(map(str, l)))
else:
    print(-1)

# 모든 순열을 구할 때 - itertools
from itertools import permutations

n = 3
l = list(range(1, n + 1))  # [1,2,3]
for p in permutations(l, n):  # 정렬 안해도 모든 순열 만들어 낸다.
    print(' '.join(map(str, p)))

data = ['A', 'B', 'C']
result = list(permutations(data, 3))  # 3개 골라 순서 있게 나열
print(result)  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'),,,
result = list(permutations(data, 2))  # 2개 골라 순서 있게 나열
