class Forme:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle(Forme):
    def __init__(self, x, y):
        super().__init__(x, y)
    def aire(self):
        return (self.x * self.y) / 2

class Rectangle(Forme):
    def __init__(self, x, y):
        super().__init__(x, y)

    def aire(self):
        return self.x * self.y