from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])  # type name, data
p = Point(11, y=22)
print(p[0] + p.y)  # 33
print(Point(x=1, y=2))  # Point(x=1, y=2)
