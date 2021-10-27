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
