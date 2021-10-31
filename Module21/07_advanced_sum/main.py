def flexible_sum(*some_data, numbers_sum=[]):
    for item in some_data:
        if isinstance(item, int):
            numbers_sum.append(item)

        else:
            item = flexible_sum(*item)

    return sum(numbers_sum)


print(flexible_sum([[1, 2, [3]], [1], 3]))
print(flexible_sum(1, 2, 3, 4, 5))


# Спасибо, разобрался. В своем коде тоже подкорректировал
def my_sum(*args):
    total_sum = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):
            for x in i_elem:
                total_sum += my_sum(x)

    return total_sum


print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum(1, 2, 3, 4, 5))
