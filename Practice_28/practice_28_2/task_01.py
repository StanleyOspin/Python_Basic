from random import randint, choice


class Robot:
    """Базовый класс Робот"""

    def __init__(self, model: str) -> None:
        print(f'Я - Робот {model}')


class CanFly:
    """Класс "Может летать", имеет аттрибуты высота и скорость, методы: взлетать, летать, приземляться"""

    def __init__(self, height: int, speed: int) -> None:
        self.height = height
        self.speed = speed
        self.distane = 0

    def take_off(self) -> int:
        self.height = randint(10, 100)
        print(f'Робот взлетел, высота: {self.height}')
        return self.height

    def fly(self) -> int:
        self.time = randint(0, 60)
        self.speed = 100
        if self.height > 0:
            self.distanse = self.speed * self.time
            print(f'Пройдена дистанция: {self.distanse}')
            return self.distanse
        else:
            self.take_off()
            self.distanse = self.speed * self.time
            print(f'Пройдена дистанция: {self.distanse}')
            return self.distanse

    def landing(self) -> int:
        self.speed = 0
        self.height = 0
        print(f'Робот приземлился: {self.height}')
        return self.height


class Scout(Robot, CanFly):
    """Класс Робот Разведчик, может летать в поиске противника"""

    def __init__(self, model: str, height: int, speed: int) -> None:
        super().__init__(model)
        CanFly.__init__(self, height, speed)

    def operate(self) -> None:
        print('Веду разведку с воздуха.')
        self.fly()


class Millitary(Robot, CanFly):
    """Класс военный Робот, может летать и защищать объект с помощью оружия"""
    weapon = ('Ракеты', 'Пушка', 'Пулемет')

    def __init__(self, model: str, height: int, speed: int) -> None:
        super().__init__(model)
        CanFly.__init__(self, height, speed)

    def operate(self) -> None:
        self.take_off()
        self.device = choice(self.weapon)
        print(f'Защищаю объект с помощью оружия: {self.device}')


robot = Scout(model='Разведчик', height=0, speed=0)
robot.operate()
print()
robot_2 = Millitary(model='Военный', height=0, speed=0)
robot_2.operate()
