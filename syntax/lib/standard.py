# 자주 사용되는 내장 함수 : import 필요 x
result = sum([1, 2, 3, 4, 5])  # 15
# 아래처럼은 못 씀 sum() takes at most 2 arguments (5 given)
min_result = min(7, 3, 5, 2)  # 2
max_result = max(7, 3, 5, 2)  # 7

# eval: 식을 계산해 수로 반환
result = eval("(3+5)*7")  # 56

# sorted() : 원본 리스트에 변화 x. 정렬된 리스트를 생성해서 반환 (느림)
result = sorted([9, 1, 8, 5, 4])  # [1, 4, 5, 8, 9]
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)  # [9, 8, 5, 4, 1]
# sorted() with key: 정렬 기준을 람다식으로 명시
array = [('최재량', 29), ('최재림', 26), ('최장환', 56)]
result = sorted(array, key=lambda t: t[1], reverse=True)  # 튜플의 1번 원소를 기준으로 제시
result = sorted(array, key=lambda t: (t[1], t[0]), reverse=True)  # 키가 같을 경우, 우선순위까지 제공
print(result)  # [('최장환', 56), ('최재량', 29), ('최재림', 26)]
