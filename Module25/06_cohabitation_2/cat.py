from familymember import FamilyMember
from random import randint, choice


class Cat(FamilyMember):
    eaten_cat_food = 0

    def eat(self):
        feed = (3, 5, 7, 10)
        feed_amount = choice(feed)
        if self.home.get_catfood() >= feed_amount:
            self.set_fullness(self.get_fullness() + 2 * feed_amount)
            self.home.set_catfood(self.home.get_catfood() - feed_amount)
            self.eaten_cat_food += feed_amount
            print('{} поел.'.format(self.get_name()))
        elif 0 < self.home.get_catfood() < feed_amount :
            self.set_fullness(self.get_fullness() + 2 * self.home.get_catfood())
            self.home.set_catfood(0)
            self.eaten_cat_food += self.home.get_catfood()
            print('{} поел.'.format(self.get_name()))
        else:
            print('Корм для кота закончился')

    def sleep(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            print('{} спал.'.format(self.get_name()))
        else:
            print('{} умер во сне от голода.'.format(self.get_name()))

    def tear_walpepper(self):
        if self.get_fullness() >= 10:
            self.set_fullness(self.get_fullness() - 10)
            print('{} драл обои.'.format(self.get_name()))
            self.home.set_dirt(self.home.get_dirt() + 5)
        else:
            print('{} был голоден и ему не до обоев.'.format(self.get_name()))

    def act(self):
        super().act()
        dice = randint(1, 6)
        if dice == 1:
            self.sleep()
        elif dice == 2:
            self.tear_walpepper()


