class MayFly:

    def __init__(self):
        self.height = 0
        self.speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def landed(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return 'Текущая высота: {}, скорость: {}'.format(self.height, self.speed)


class Butterfly(MayFly):

    def __init__(self):
        super().__init__()

    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(MayFly):

    def __init__(self):
        super().__init__()

    def take_off(self):
        self.height = 500
        self.speed = 1000

    def landed(self):
        self.height = 0
        if self.height == 0 and self.speed > 0:
            print('Взрыв!!!')
            self.speed = 0

    def explode(self):
        print('Вспышка, дым, грохот ......')


butterfly = Butterfly()
print(butterfly)
butterfly.take_off()
butterfly.fly()
print(butterfly)

rocket = Rocket()
print(rocket)
rocket.take_off()
rocket.landed()
rocket.explode()
print(rocket)