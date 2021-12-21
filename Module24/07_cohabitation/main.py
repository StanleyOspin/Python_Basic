from random import randint


class Human(): # TODO Аналогично предыдущему

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.home = None

    def __str__(self):
        return '{}, сытость {}.'.format(self.name, self.fullness)

    def eat(self):
        if home.food >= 10:
            print('{} поел.'.format(self.name))
            self.fullness += 10
            home.food -= 10

    def work(self):
        self.fullness -= 10
        home.money += 50
        print('{} сходил на работу.'.format(self.name))

    def play(self):
        self.fullness -= 10
        print('{} играл в игры на смартфоне.'.format(self.name))

    def shopping(self):
        if home.money >= 50:
            home.food += 50
            print('{} купил еды.'.format(self.name))
            home.money -= 50
        else:
            print('Денег нет')

    def life(self):  # TODO лучше назвать "действовать" (act)
        if self.fullness <= 0:
            print('{} умер.'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif home.food < 10:
            print('{} нет еды, нужно идти в магазин.'.format(self.name))
            self.shopping()
        elif home.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.play()
        else:
            self.play()

    def settle_in_the_house(self, home):
        self.home = home


class House():
    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'В доме, еды осталось {}, денег в тумбочке {}.'.format(home.food, home.money)


characters = [Human('Иван Царевич'), Human('Кащей Бессмертный')]

home = House()
for character in characters:
    character.settle_in_the_house(home)

for day in range(1, 21):
    print('=============== день {} ================'.format(day))
    for character in characters:
        character.life()
        print(character)
        print(home)
