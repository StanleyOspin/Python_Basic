from collections.abc import Iterable


# version 1
class My_Iterator:
    def __init__(self, limit: int) -> None:
        self.__number = 0
        self.__limit = limit

    def __iter__(self) -> Iterable[int]:
        self.number = 1
        return self

    def __next__(self) -> int:
        if self.__number < self.__limit:
            self.__number += 1
            return self.__number ** 2
        else:
            raise StopIteration


squares = My_Iterator(10)
for item in squares:
    print(item, end=' ')

print()


# version 2
def my_generator(limit: int) -> Iterable[int]:
    number = 1
    for i in range(number, limit + 1):
        yield i ** 2
        number += 1


for item in my_generator(10):
    print(item, end=' ')

print()
# version 2
number = 10
square = (item ** 2 for item in range(1, number + 1))

for i in square:
    print(i, end=' ')
