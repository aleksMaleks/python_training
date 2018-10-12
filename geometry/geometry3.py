from geom2d import *

l = []

for i in range(-5, 6):
    l.append(Point(i, i*i))


print(l)
print()



for el in l:
    print(el)
print()



for el in l:
    el.y = -el.y
print(l)
print()



l1 = []
l2 = []
for i in range(-5, 6):
    l.append(Point(i, i*i))

l2 = []
for el in l:
    l2.append(Point(el.x, -el.y))
print(l)
print(l2)
print()



# выварачиваем на изнанку (list comprehension)
l1 = []
l2 = []
l = [Point(i, i*i) for i in range(-5, 6)]

l2 = [Point(el.x, -el.y) for el in l]

print(l)
print(l2)