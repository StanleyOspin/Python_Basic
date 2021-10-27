def flexible_sum(numbers_sum, *some_data):
    some_data = list(some_data)

    for item in some_data:
        if isinstance(item, int):
            numbers_sum.append(item)

        else:
            item = flexible_sum(numbers_sum, *item)

    return sum(numbers_sum)


numbers_sum = []
numbers_sum = flexible_sum(numbers_sum, [[1, 2, [3]], [1], 3])
# numbers_sum = flexible_sum(numbers_sum, 1, 2, 3, 4, 5)
print(numbers_sum)


# TODO другой вариант решения:
def my_sum(*args):
    total_sum = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):
            for x in i_elem:
                total_sum += my_sum(x)

    return total_sum
