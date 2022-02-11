numbers = [10, 11]


def my_for(numbers):
    iterable = iter(numbers)
    next_element = True
    while next_element:
        try:
            print(next(iterable))
        except StopIteration:
            next_element = False


my_for(numbers)

