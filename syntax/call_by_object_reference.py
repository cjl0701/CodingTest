# 자바와 마찬가지로 dic,list 같은 mutable한 객체가 전달되면 call-by-referce로 작동
class OBJ(object):
    def __init__(self, x):
        self.x = x


def func(o):  # o가 obj를 가리킴
    o.x = -1  # o가 가리키는 값 변경


obj = OBJ(1)
print(obj.x)  # 1
func(obj)
print(obj.x)  # -1


# immutable한 객체가 인자로 전달되면 call-by-value처럼 작동한다.
# 객체 전달이니 값이 변해야하지 않을까??
def print_val(val):  # val 변수 생성, i와 같은 객체 가리킴.
    val += 10  # 값이 증가하는게 아니라, 새로운 객체 12의 인스턴스가 생성되며 val 변수는 그것을 가리킴
    print(val)


i = 2
print_val(i)  # 12
print(i)  # 2

"""
def change(t):  # 지역변수 t는 객체 10을 가리킴
    t = 20  # 가리키는 객체 변경
    t += 1


x = 10
print(x)  # 10
change(x)
print(x)  # 10


def func(glo2):
    a = 1  # 지역 변수 선언
    glo2 = 2  # 매개변수가 다른 객체를 참조하게 됐다.
    glo2 += 1
    global glo  # 전역 변수 사용
    glo += 1


glo = 0
glo2 = 0
func(glo2)
print(glo)  # 1
print(glo2)  # 0


def func1():
    array.append(6)  # 전역 변수에 추가
    print(array)


def func2():
    array = [3, 4, 5]  # 전역 변수의 참조값 변경 불가 -> 지역 변수 생성
    print(array)


def func3():
    global array  # 전역 변수를 참조하겠다.
    array = [3, 4, 5]  # 참조값을 바꿨다!
    print(array)


array = [1, 2, 3, 4, 5]
func1()  # [1, 2, 3, 4, 5, 6]
print(array)  # [1, 2, 3, 4, 5, 6]
func2()  # [3,4,5]
print(array)  # [1, 2, 3, 4, 5, 6]
func3()  # [3,4,5]
print(array)  # [3, 4, 5]
"""
