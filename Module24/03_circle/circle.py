from math import pi


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
        self.square = pi * (self.r ** 2)
        self.length = 2 * pi * self.r

    def circle_square(self):
        return round(self.square, 2)

    def circle_length(self):
        return round(self.length, 2)

    def increase_k_times(self, k):
        self.increased = k * pi * (self.r ** 2)
        return round(self.increased, 2)

    def intersection(self, other):
        if (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2:
            print('Окуржности пересекаются')
        else:
            print('Окуржности не пересекаются')
