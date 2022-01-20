from random import randint, choice


class FamilyMember:
    __eaten = 0

    def __init__(self, name, fullness):
        self.set_name(name)
        self.set_fullness(fullness)
        self.home = None

    def __str__(self):
        return '{}:\nстепень сытости - {}'.format(self.__name, self.__fullness)

    def set_name(self, name):
        self.__name = name

    def set_fullness(self, fullness):
        self.__fullness = fullness

    def get_name(self):
        return self.__name

    def get_fullness(self):
        return self.__fullness

    def settle_in_the_house(self, home):
        self.home = home

    def get_eaten(self):
        return self.__eaten

    def eat(self):
        meal = (10, 20, 30)
        meal_amount = choice(meal)
        if self.home.get_food() >= meal_amount:
            self.__fullness += meal_amount
            self.home.set_food(self.home.get_food() - meal_amount)
            self.__eaten += meal_amount
            return True

        elif meal_amount > self.home.get_food() > 0:
            self.__fullness += self.home.get_food()
            self.home.set_food(0)
            self.__eaten += self.home.get_food()
            return True
        else:
            print('Еда закончилась, не поел!')
            return False

    def act(self):
        if self.__fullness < 0:
            print('{} - степень голода критическая, наступила смерть.'.format(self.__name))

        elif self.get_fullness() < 20:
            self.eat()
