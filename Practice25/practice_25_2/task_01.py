class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'Coodinates: X = {}, Y = {}'.format(self.__x, self.__y)

    def get_coordinates(self):
        return self.__x, self.__y

    def set_coordinates(self, x, y):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coordinates must be integer')


point = Point()
point.set_coordinates(10, 5)
print(point())