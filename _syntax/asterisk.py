import sys
from functools import reduce

# asterisk
""" 1. 리스트형 컨테이너 타입의 데이터를 반복 확장 """
zeros_list = [0] * 100  # [0,0,0,,]
zeros_tuple = (0,) * 100  # (0,0,0,,)
# 리스트 확장
my_list = [1, 2, 3]
vector_list = [[1, 2, 3]]
my_list *= 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
vector_list *= 3  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# 리스트 3배 확장 후 연산
vector_list = [[1, 2, 3]]
for i, vector in enumerate(vector_list * 3):
    print("{0} scalar product of vector: {1}".format((i + 1), [(i + 1) * e for e in vector]))
    # 1 scalar product of vector: [1, 2, 3]
    # 2 scalar product of vector: [2, 4, 6]
    # 3 scalar product of vector: [3, 6, 9]

""" 2. 가변인자 : packing"""


def func(a, *args, **kwargs):  # kwargs:임의의 갯수와 임의의 키값을 갖는 인자 전달
    print(a)
    print(args)  # (2, 3, 4) 튜플 타입
    print(kwargs)  # {'x': 1, 'y': 2, 'z': 3} 딕셔너리 타입


func(1, 2, 3, 4, x=1, y=2, z=3)

""" 3. 컨테이너 타입의 데이터를 unpacking 할 때 """
data = ([1, 2], [3, 4], [5, 6])
print(*data)  # [1, 2] [3, 4] [5, 6]

for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(data)  # (1, 3, 5) (2, 4, 6)


# unpacking해서 가변인자로 전달하기
def func2(*numbers):
    p = reduce(lambda x, y: x * y, numbers)
    print(numbers)  # tuple
    # numbers[0]=1 할당 불가
    return p


primes = [2, 3, 5, 7, 11, 13]
func2(*primes)  # 30030 - unpacking 되어 인자들이 전달됨
func2(primes)  # [2,3,5,7,11,13] - 인자가 리스트 하나이므로.


def func3(**kwargs):
    host = kwargs['Host']
    print(type(kwargs))  # <class 'dict'>
    kwargs['new'] = 'in func3'
    print(kwargs)  # {'Content-Length': 348, 'Host': 'http://www.hello.com', 'new': 'in func3'}


headers = {'Content-Length': 348, "Host": 'http://www.hello.com'}
func3(**headers)  # dict type 언패킹
print(headers)  # {'Content-Length': 348, 'Host': 'http://www.hello.com'}

# 리스트나 튜플의 데이터를 다른 변수에 가변적으로 unpacking
# 우변의 리스트가 unpacking 된 후, *변수에 리스트로 packing됨 (가변인자 packing과 같은 개념)
numbers = [1, 2, 3, 4, 5, 6]
# unpacking의 좌변은 리스트 또는 튜플의 형태를 가져야 하므로, 단일 unpacking의 경우 *a가 아닌 *a, 사용
*a, = numbers  # [1, 2, 3, 4, 5, 6]
*a, b = numbers  # [1, 2, 3, 4, 5] / 6
a, *b = numbers  # 1 / [2, 3, 4, 5, 6]
a, *b, c = numbers  # 1 / [2, 3, 4, 5] / 6

# 활용
op, *num = sys.stdin.readline().split()  # num에 가변적으로 할당 됨. 데이터가 1개면 할당이 안될 수도
