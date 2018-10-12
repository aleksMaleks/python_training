from geom2d import *


l1 = [Point(2, 1), Point(0, 0), Point(1, 2)]
#l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
#l2 = l1

# l2 = list(l1)
# l2[0] = Point(0, 0)
#
# print(l1)
# print(l1 == l2)

# l2 = sorted(l1)
# print("ok")
# print(l1)
# print(l2)

def x(p):
    return p.x

l2 = sorted(l1, key=x)
print("Сортирвка по x:")
print(l1)
print(l2)


def y(p):
    return p.y

l2 = sorted(l1, key=y)
print("Сортирвка по y:")
print(l1)
print(l2)


# лямбда выражение
l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]

#l2 = sorted(l1, key=lambda p: p.x)
l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

print("Лямбда выражение:")
print(l1)
print(l2)


