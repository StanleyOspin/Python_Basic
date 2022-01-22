from familymember import FamilyMember
from random import randint, choice


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

    def get_furcoat(self):
        return self.__fur_coat

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

    def buy_food(self):
        meal = (30, 40, 50, 60)
        meal_amount = choice(meal)
        if self.get_fullness() >= 10:
            if self.home.get_money() >= meal_amount:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_money(self.home.get_money() - meal_amount)
                self.home.set_food(self.home.get_food() + meal_amount)
                print('{} купила еды'.format(self.get_name()))

            elif meal_amount > self.home.get_money() > 0:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_money(0)
                self.home.set_food(self.home.get_money())
            else:
                print('Денег на еду нет')

        else:
            print('{} пошла купить еды, но не хватило сытости до магазина не дошла.'.format(self.get_name()))

    def buy_catfood(self):
        if self.get_fullness() >= 10:
            if self.home.get_money() >= 10:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_money(self.home.get_money() - 10)
                self.home.set_catfood(self.home.get_catfood() + 10)
                print('{} купила еды для кота'.format(self.get_name()))
            else:
                print('Денег на корм для кота нет')
        else:
            print('{} пошла купить еды для кота, но была сильно голодна до магазина не дошла.'.format(self.get_name()))

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
                print('Для поднятия настроения можно хотя бы кота погладить')
                self.pet_a_cat()
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
        if self.home.get_food() < 50:
            self.buy_food()
        elif self.home.get_catfood() < 30:
            self.buy_catfood()
        elif self.home.get_dirt() > 150:
            self.cleanning()
        elif self.__happiness < 50:
            self.buy_furcoat()
        elif self.__happiness < 10:
            print('{} умерла от депрессии.'.format(self.get_name()))

        elif dice == 1:
            self.cleanning()
        elif dice == 2:
            self.pet_a_cat()
        elif dice == 3:
            self.buy_furcoat()
        elif dice == 4:
            self.buy_food()
        elif dice == 5:
            self.buy_catfood()
        elif self.home.get_dirt() >= 90:
            self.__happiness -= 10
