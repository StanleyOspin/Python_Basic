from familymember import FamilyMember
from random import randint, choice


class Baby(FamilyMember):

    def __init__(self, name, fullness, happiness=100, performance=True):
        super().__init__(name, fullness)
        self.set_happiness(happiness)
        self.set_performance(performance)

    def __str__(self):
        return super().__str__() + '\nстепень счастья {}'.format(self.__happiness)

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, happiness):
        self.__happiness = happiness

    def set_performance(self, performance):
        self.__performance = performance

    def eat(self):

        if super().eat():
            print('{} поел.'.format(self.get_name()))

    def go_to_school(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            dice = randint(1, 5)
            if dice < 4:
                self.home.set_performance = False
                print('День не удался, {} получил оценку {}.'.format(self.get_name(), dice))
            else:
                self.home.set_performance = True
                print('День удался, {} получил оценку {}.'.format(self.get_name(), dice))

        else:
            print('{} должен был идти в школу, но обессилел из-за недостаточной сытости.'.format(self.get_name()))

    def play(self):
        if self.get_fullness() >= 10:
            if self.__performance:
                self.set_fullness(self.get_fullness() - 10)
                self.__happiness += 30
                print('{} играл в игры на компе.'.format(self.get_name()))
            else:
                print('За плохую успеваемость в комп поиграть не дали')
        else:
            print('{} не получилось играть, т.к. не хватило сытости.'.format(self.get_name()))

    def entertainment(self):
        if self.get_fullness() >= 10:
            if self.__performance:
                self.set_fullness(self.get_fullness() - 10)
                self.__happiness += 50
                print('{} ходил в парк развлечений.'.format(self.get_name()))
            else:
                print('За плохую успеваемость в парк развлечений не повели, сидел дома')
                print('Для поднятия настроения можно хотя бы кота погладить')
                self.pet_a_cat()
        else:
            print('{} в парк развлечений не ходил, т.к. не хватило сытости.'.format(self.get_name()))

    def pet_a_cat(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            print('{} погладил кота.'.format(self.get_name()))
            self.__happiness += 5

    def act(self):
        super().act()
        day = randint(1, 7)

        if day < 6:
            self.go_to_school()
        elif day > 5:
            self.entertainment()
        elif self.__happiness < 20:
            self.play()
        elif self.__happiness < 10:
            print('{} умер от депрессии.'.format(self.get_name()))
        elif self.home.get_dirt() >= 90:
            self.__happiness -= 10
