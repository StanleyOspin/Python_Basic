class Water:

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava

    def __str__(self):
        return Fire.name


class Earth():  # TODO скобки не нужны
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Air():  # TODO скобки не нужны
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return Air.name


class Wood:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Coal()
        elif isinstance(other, Earth):
            return Forest()


class Steam:
    name = 'Пар'
    answer = 'Пар'

    def __str__(self):
        return Steam.name


class Dirt:
    answer = 'Грязь'


class Storm:
    answer = 'Шторм'


class Lightning:
    name = 'Молния'
    answer = 'Молния'

    def __str__(self):
        return Lightning.name


class Lava:
    answer = 'Лава'


class Dust:
    answer = 'Пыль'


class Coal:
    answer = 'Уголь'


class Forest:
    answer = 'Лес'


air = Air()  # TODO называйте переменные полными словами
fire = Fire()
c = Earth()
d = Water()
e = Wood()
result = air + fire

if not result:
    print(e)
else:
    print(result.answer)

# TODO Пример вывода:
print(f'{air} + {fire} = {result}')
