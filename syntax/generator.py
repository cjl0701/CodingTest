# yield: next로 진행 시, yield를 만나는 순간 이후의 진행을 양보함!
def func():
    print("출력 1")
    yield 1  # 이 키워드를 적는 순간 기본적으로는 실행 안됨.
    print("출력 2")
    yield 2
    print("출력 3")
    yield 3


generator = func()  # <class 'generator'> 함수 호출 시 generator라는 객체 리턴

return_value = next(generator)
print(return_value)
return_value = next(generator)
print(return_value)
return_value = next(generator)
print(return_value)
# next(generator)  # StopIteration 에러. iteration이 끝났는데 왜 호출하냐!

# 실 사용 시, 반복문 형태로 사용됨
for i in func():
    print(i)

# iterator이므로 일회용!
print("generator는")
for i in generator:  # 반복x
    print(i)
print("일회용")

iterator = reversed([1, 2, 3])
for i in iterator:
    print(i)  # 3,2,1
for i in iterator:  # 반복 x
    print(i)


def reverse(리스트):
    for i in range(len(리스트)):
        yield 리스트[-i - 1]  # 거꾸로 된 list를 새로 만드는 게 아니다!


generator = reverse([1, 2, 3])
for i in generator:
    print(i)

numbers = [1, 2, 3, 4, 5, 6]
# join에 iterator 객체를 전달하기 위해
print("::".join(map(str, numbers)))  # 1::2::3::4::5::6


def generator(n):
    i = 0
    while i < n:
        yield i  # 여기서 일단 반환하고 멈춤, 여기서부터 재시작
        i += 1


# 실 사용 시에는, 반복문 형태로 사용 - stopIteration이 나올 때까지 반복
for x in generator(5):
    print(x)  # 0 1 2 3 4
