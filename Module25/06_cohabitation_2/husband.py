from familymember import FamilyMember
from random import randint, choice


class Husband(FamilyMember):

    def __init__(self, name, fullness, happiness=100, earned=0):
        super().__init__(name, fullness)
        self.set_happiness(happiness)
        self.earned = earned

    def __str__(self):
        return super().__str__() + '\nстепень счастья {}'.format(self.__happiness)

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, happiness):
        self.__happiness = happiness

    def eat(self):

        if super().eat():
            print('{} поел.'.format(self.get_name()))

    def buy_food(self):
        meal = (10, 20, 30)
        meal_amount = choice(meal)
        if self.get_fullness() >= 10:
            if self.home.get_money() >= meal_amount:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_money(self.home.get_money() - meal_amount)
                self.home.set_food(self.home.get_food() + meal_amount)
                print('{} купил еды'.format(self.get_name()))

            elif meal_amount > self.home.get_money() > 0:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_money(0)
                self.home.set_food(self.home.get_money())
            else:
                print('Денег на еду нет, надо идти на работу')

        else:
            print('{} пошел купить еды, но не хватило сытости до магазина не дошел.'.format(self.get_name()))

    def buy_catfood(self):
        if self.get_fullness() >= 10:
            if self.home.get_money() >= 10:
                self.set_fullness(self.get_fullness() - 10)
                self.home.set_money(self.home.get_money() - 10)
                self.home.set_catfood(self.home.get_catfood() + 10)
                print('{} купил еды для кота'.format(self.get_name()))
            else:
                print('Денег на корм для кота нет, надо идти на работу')
        else:
            print('{} пошел купить еды для кота, но был сильно голоден до магазина не дошел.'.format(self.get_name()))

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
            self.earned += 150
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
        # TODO для мужа также базовым действием не зависящим от случайностей должно быть зарабатывание денег, это
        #  критически важный ресурс для семьи
        dice = randint(1, 6)
        if self.__happiness < 10:
            print('{} умер от депрессии.'.format(self.get_name()))
        elif self.__happiness < 50:
            self.pet_a_cat()
        elif self.home.get_food() < 20:
            self.buy_food()
        elif self.home.get_catfood() < 10:
            self.buy_catfood()
        elif self.home.get_money() < 500:
            self.work()
        elif self.home.get_dirt() >= 90:
            self.__happiness -= 10

        elif dice == 1:
            self.work()
        elif dice == 2:
            self.play()
        elif dice == 3:
            self.buy_food()
        elif dice == 4:
            self.buy_catfood()
        elif dice == 5:
            self.pet_a_cat()
