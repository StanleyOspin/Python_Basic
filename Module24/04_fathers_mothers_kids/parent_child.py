from random import randint


class Parents:

    def __init__(self, name, age, children):
        self.parent_name = name
        self.parent_age = age
        self.children = children

    def check_age(self):
        for child in self.children:
            if self.parent_age - child.child_age < 16:
                raise ValueError('Разница в возресте родителя и ребенка должна быть не менее 16 лет.')

    def children_quantity(self):
        return len(self.children)

    def print_info(self):
        print('\nЯ {}, мне {} лет и у меня {} детей:\n'.format(self.parent_name, self.parent_age,
                                                               self.children_quantity()))
        year = ''
        for child in self.children:
            child = (child.child_name, child.child_age)
            if child[1] == 1:
                year = 'год'
            elif child[1] in [2, 3, 4]:
                year = 'года'
            else:
                year = 'лет'
            print('{} - {} {}'.format(child[0], child[1], year))

    def child_feed(self):
        for child in self.children:
            if child.hunger == 0:
                print('\n{} хочет кушать, нужно покормить.'.format(child.child_name))
                print('{} накормил {}.'.format(self.parent_name, child.child_name[0:-1] + 'y'))
                child.hunger += 4
            else:
                child.hunger -= 1

    def child_make_calm(self):
        for child in self.children:
            if child.calmness == 0:
                print('\n{} плачет, нужно успокоить.'.format(child.child_name))
                print('{} успокоил {}.'.format(self.parent_name, child.child_name[0:-1] + 'y'))
                child.calmness += 4
            else:
                child.calmness = -1


class Child:

    def __init__(self, child_name, child_age):
        self.child_name = child_name
        self.child_age = child_age
        self.calmness = randint(0, 4)
        self.hunger = randint(0, 4)

