from familymember import FamilyMember
from random import randint


class Husband(FamilyMember):
    __earned = 0

    def __init__(self, name, fullness, happiness=100):
        super().__init__(name, fullness)
        self.set_happiness(happiness)

    def __str__(self):
        return super().__str__() + '\nстепень счастья {}'.format(self.__happiness)

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, happiness):
        self.__happiness = happiness

    def get_earned(self):
        return self.__earned

    def eat(self):

        if super().eat():
            print('{} поел.'.format(self.get_name()))

    def play(self):
        if self.get_fullness() >= 10:

            self.set_fullness(self.get_fullness() - 10)
            self.__happiness += 20
            print('{} играл в игры на компе.'.format(self.get_name()))

        else:
            print('{} не получилось играть, т.к. не хватило сытости.'.format(self.get_name()))

    def work(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            self.home.set_money(self.home.get_money() + 150)
            print('{} сходил на работу, денег стало больше, сейчас в тумбочке {}.'.format(self.get_name(),
                                                                                          self.home.get_money()))
            self.__earned = 150
        else:
            print('{} должен был идти на работу, но не смог из-за недостаточной сытости.'.format(self.get_name()))

    def pet_a_cat(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            print('{} погладил кота.'.format(self.get_name()))
            self.__happiness += 5

        else:
            print('{} проголодался так, что не в состоянии гладить кота.'.format(self.get_name()))

    def act(self):
        super().act()

        dice = randint(1, 6)
        if self.home.get_money() < 500:
            self.work()
        elif self.__happiness < 50:
            self.play()
        elif self.__happiness < 10:
            print('{} умер от депрессии.'.format(self.get_name()))

        elif dice == 1:
            self.work()
        elif dice == 2:
            self.play()
        elif dice == 5:
            self.pet_a_cat()
        elif self.home.get_dirt() >= 90:
            self.__happiness -= 10
