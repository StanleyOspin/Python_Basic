class Primes:
    def __init__(self, maximal):
        self.counter = 0
        self.maximal = maximal
        self.number = 2

    def __iter__(self):
        self.counter = 0
        self.number = 2
        return self.number

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.maximal:
                raise StopIteration
            elif self.number %

prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')
