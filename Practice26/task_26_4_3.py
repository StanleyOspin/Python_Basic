import math

class Primes:
    def __init__(self, maximal):
        self.counter = 0
        self.maximal = maximal
        self.number = 2

    def __iter__(self):
        self.counter = 0
        self.number = 2
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            square = math.ceil(self.number ** 0.5)
            while self.counter < self.maximal:
                for i in range(2, square + 1):
                    if self.number % square == 0:
                        break
                    else:
                        self.number += 1
        return self.number


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')
