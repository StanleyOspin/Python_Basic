class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False

        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def take_away_potatoes(self):
        self.potatoes = []


class Gardener():

    def __init__(self, name, potatogarden):
        self.name = name
        self.potatogarden = potatogarden

    def care_of_potatoes(self):

        if all([i_potato.state == 0 or i_potato.state == 1 for i_potato in self.potatogarden]):
            print('{} поливает картошку!\n'.format(self.name))
            my_garden.grow_all()

        elif all([i_potato.state == 2 for i_potato in self.potatogarden]):
            print('{} окучивает картошку!\n'.format(self.name))
            my_garden.grow_all()

        elif my_garden.are_all_ripe():
            print('{} пошел копать картошку!\n'.format(self.name))
            gardener.harvest()

    def harvest(self):
        my_garden.take_away_potatoes()
        print('Урожай собран')


my_garden = PotatoGarden(5)
gardener = Gardener('дядя Миша', my_garden.potatoes)

for _ in range(4):
    gardener.care_of_potatoes()
    print()

print('Состояние грядки: ', my_garden.potatoes)
