import math


class Geometry:
    def __init__(self):
        pass

    def distance(self, x1, x2, y1, y2):
        return math.sqrt((y1 - x1) ** 2 + (y2 - x2) ** 2)

    def middle(self, a, b):
        x = (a[0] + b[0]) / 2
        y = (a[1] + b[1]) / 2
        return [x, y]

    def triangle_perimeter(self, a, b, c):
        return a + b + c

    def triangle_isoceles(self, a, b, c):
        if a == b or a == c or b == c:
            return True
        return False