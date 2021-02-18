class SoccerPlayer(object):
    # 자바와 다르게 property field 명시x
    # 생성자.
    def __init__(self, name, position, back_number):  # self: this
        self.name = name  # 하긴 여긴 보면 알 수 있으니.
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다: From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    # toString
    def __str__(self):
        return "Hello, my name is %s. I play in %s in center" % (self.name, self.position)


son = SoccerPlayer("heongmin", "MF", 10)  # __init__
print(son)  # __str__
print("현재 등번호: ", son.back_number)
son.change_back_number(5)
print("현재 등번호: ", son.back_number)


class Person(object):
    def __init__(self):
        self.__age = 0  # private

    @property
    def age(self):
        return self.__age  # 참조만 가능

    @age.setter  # 이게 없으면 __age 변경 불가
    def age(self, value):
        self.__age = value


jaelyang = Person()
jaelyang.age = 29  # @age.setter 덕
