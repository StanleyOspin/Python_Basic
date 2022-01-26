class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return '\nМодель корабля: {}'.format(self.__model)

    def sail(self):
        print('Корабль куда-то пошёл!')


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('Корабль атаковал с помощью оружия {}'.format(self.gun))


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.loadness = 0

    def load(self):
        print('\nЗагружаем корабль')
        self.loadness += 1
        print('Текущая загруженность {}'.format(self.loadness))

    def unload(self):
        print('\nРазгружаем корабль')
        if self.loadness > 0:
            self.loadness -= 1
        else:
            print('Корабль уже разгружен')
        print('Текущая загруженность {}'.format(self.loadness))


warship = WarShip('Ракетоносец', 'ракета')
print(warship)
warship.sail()
warship.attack()
cargoship = CargoShip('Сухогруз')
print(cargoship)
cargoship.load()
cargoship.unload()
