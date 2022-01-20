from familymember import FamilyMember
from random import randint


class Wife(FamilyMember):
    __fur_coat = 0

    def __init__(self, name, fullness, happiness=100):
        super().__init__(name, fullness)
        self.set_happiness(happiness)

    def __str__(self):
        return super().__str__() + '\nстепень счастья - {}'.format(self.__happiness)

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, happiness):
        self.__happiness = happiness

    def eat(self):

        if super().eat():
            print('{} поела.'.format(self.get_name()))

    def get_fur_coats(self):
        return self.__fur_coat

    def cleanning(self):
        if self.get_fullness() >= 10:
            if self.home.get_dirt() <= 100:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_dirt(0)
                print('{} навела дома порядок.'.format(self.get_name()))
            elif self.home.get_dirt() > 100:
                self.set_fullness(self.get_fullness() - 10)
                print('{} усердно убиралась, но кое-что еще не в порядке.'.format(self.get_name()))
                self.home.set_dirt(self.home.get_dirt() - 100)
        else:
            print('{} из-за голода не смогла привести дом в порядок.'.format(self.get_name()))

    def buy_furcoat(self):
        if self.get_fullness() >= 10:
            if self.home.get_money() >= 400:
                self.__happiness += 60
                self.home.set_money(self.home.get_money() - 350)
                self.__fur_coat += 1
                print('{} Купила шубу.'.format(self.get_name()))

            else:
                print(
                    '{} хотела купить шубу, но денег маловато, шубу не берем, накопим деньжат.'.format(self.get_name()))
        else:
            print('{} хотела купить шубу, сейчас за гамбургер отдала бы все деньги, шуба подождет.'.format(
                self.get_name()))

    def pet_a_cat(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            print('{} погладила кота.'.format(self.get_name()))
            self.__happiness += 5

        else:
            print('{} проголодалась так, что не в состоянии гладить кота.'.format(self.get_name()))

    def act(self):
        super().act()
        dice = randint(1, 6)
        if self.__happiness < 10:
            print('{} умерла от депрессии.'.format(self.get_name()))
        elif self.__happiness < 50:
            self.pet_a_cat()
        elif self.home.get_dirt() > 150:
            self.cleanning()
        elif self.home.get_dirt() >= 90:
            self.__happiness -= 10
        elif dice == 1:
            self.cleanning()
        elif dice == 2:
            self.pet_a_cat()
        elif dice == 3:
            self.buy_furcoat()
