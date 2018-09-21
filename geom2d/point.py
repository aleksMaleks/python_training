from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x # _x переменная параметр, а x атрибут объекта self
        self.y = _y # _y переменная параметр, а y атрибут объекта self

    def distance(self, p2): # эта функци стала методом
        dx = p2.x - self.x # self - это объект в котором этот метод вызывается
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


