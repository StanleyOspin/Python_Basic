def new_tuple(some_tuple, element):
    if element in some_tuple:
        if some_tuple.count(element) > 1:
            first_index = some_tuple.index(element)
            second_index = some_tuple.index(element, first_index + 1) + 1
            return some_tuple[first_index:second_index]
        else:
            first_index = some_tuple.index(element)
            return some_tuple[first_index:]
    else:
        return ()


element = int(input('Случайный элемент: '))
# print(new_tuple((1,2,3,5,6), element))
print(new_tuple((1, 4, 3, 5, 6, 4, 9, 2), element))
# print(new_tuple((1, 2, 3, 4, 5, 1, 2, 9), element))
