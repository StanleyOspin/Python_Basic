class House:
    def __init__(self, money=100, food=50, catfood=30, dirt=0):
        self.set_money(money)
        self.set_food(food)
        self.set_catfood(catfood)
        self.set_dirt(dirt)

    def set_money(self, money):
        self.__money = money

    def set_food(self, food):
        self.__food = food

    def set_catfood(self, catfood):
        self.__catfood = catfood

    def set_dirt(self, dirt):
        self.__dirt = dirt

    def get_money(self):
        return self.__money

    def get_food(self):
        return self.__food

    def get_catfood(self):
        return self.__catfood

    def get_dirt(self):
        return self.__dirt

    def __str__(self):
        return 'В доме:\nденег - {}\nеды - {}\nкорм для кота - {}\nгрязи - {}.'.format(self.__money, self.__food,
                                                                                       self.__catfood, self.__dirt)

    def act(self):
        self.__dirt += 5
