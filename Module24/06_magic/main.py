class Water:

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava


class Earth():
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Air():
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Wood:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Coal()
        elif isinstance(other, Earth):
            return Forest()


class Steam:
    answer = 'Пар'


class Dirt:
    answer = 'Грязь'


class Storm:
    answer = 'Шторм'


class Lightning:
    answer = 'Молния'


class Lava:
    answer = 'Лава'


class Dust:
    answer = 'Пыль'


class Coal:
    answer = 'Уголь'


class Forest:
    answer = 'Лес'


a = Air()
b = Fire()
c = Earth()
d = Water()
e = Wood()
f = a + b

if not f:
    print(e)
else:
    print(f.answer)
