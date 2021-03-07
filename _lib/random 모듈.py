import random

random.random()  # 0이상 ~ 1미만
random.randrange(1, 7)  # 1이상 7미만
abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)  # 순서형 자료를 섞어놓음
print(abc)
random.shuffle(abc)
print(abc)

random.choice(abc)  # 아무 원소나 하나 뽑아줌

# 1~500 사이의 숫자 3개 랜덤하게 뽑기
testcase = [random.randrange(1, 501) for _ in range(3)]
