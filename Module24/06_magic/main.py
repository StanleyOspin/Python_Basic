class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm

    def __str__(self):
        return Water.name


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


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()

    def __str__(self):
        return Earth.name


class Air:
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
    name = 'Дерево'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Coal()
        elif isinstance(other, Earth):
            return Forest()

    def __str__(self):
        return Wood.name


class Steam:
    name = 'Пар'
    answer = 'Пар'

    def __str__(self):
        return Steam.name


class Dirt:
    name = 'Грязь'
    answer = 'Грязь'

    def __str__(self):
        return Dirt.name


class Storm:
    name = 'Шторм'
    answer = 'Шторм'

    def __str__(self):
        return Storm.name


class Lightning:
    name = 'Молния'
    answer = 'Молния'

    def __str__(self):
        return Lightning.name


class Lava:
    name = 'Лава'
    answer = 'Лава'

    def __str__(self):
        return Lava.name


class Dust:
    name = 'Пыль'
    answer = 'Пыль'

    def __str__(self):
        return Dust.name


class Coal:
    name = 'Уголь'
    answer = 'Уголь'

    def __str__(self):
        return Coal.name


class Forest:
    name = 'Лес'
    answer = 'Лес'

    def __str__(self):
        return Forest.name


air = Air()
fire = Fire()
earth = Earth()
water = Water()
wood = Wood()
result = air + water

print(f'{air} + {water} = {result}')
