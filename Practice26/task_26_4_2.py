from random import random


class MyIterator:

    def __init__(self, quantity):
        self.counter = 0
        self.current = random()
        self.next = random()
        self.quantity = quantity

    def __iter__(self):
        self.counter = 0
        self.current = random()
        self.next = random()

        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > quantity:
                raise StopIteration

            self.current, self.next = self.next, self.current + self.next
        return self.current


quantity = int(input('Кол-во элементов: '))
my_iter = MyIterator(quantity)

print('Элементы итератора: ')
for i_elem in my_iter:
    print(round(i_elem, 2))
