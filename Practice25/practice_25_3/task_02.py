class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\nМодель робота {}'.format(self.__model)


class Hoover(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.occupancy = 0

    def operate(self):
        if self.occupancy == 0:
            print('\nНачал уборку')
            self.occupancy += 10
        elif self.occupancy < 100:
            print('Делаю уборку')
            self.occupancy += 10
        elif self.occupancy == 100:
            print('\nМешок полный, требуется очистка')
            print('Мешок для мусора заменили.')
            self.occupancy = 0


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('\nЗащищаю объект с помощью оружия {}'.format(self.gun))


class SubmarineRobot(WarRobot):
    def __init__(self, model, gun, deepth):
        super().__init__(model, gun)
        self.deepth = deepth

    def operate(self):
        super().operate()
        print('Глубина {} метров'.format(self.deepth))


warrobot = WarRobot('Vally', 'пушка')
print(warrobot)
warrobot.operate()
subrobot = SubmarineRobot('Водолаз', 'торпеда', 100)
print(subrobot)
subrobot.operate()
hoover = Hoover('Пылесос')
print(hoover)
for _ in range(15):
    hoover.operate()
