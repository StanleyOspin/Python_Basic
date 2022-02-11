def find_number(list_1: list, list_2: list, to_find: int) -> int:
    for x in list_1:

        for y in list_2:
            result = x * y
            yield x, y, result
            if result == to_find:
                return print('Found!!!')


to_find = 56
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
my_generator = find_number(list_1, list_2, to_find)

for item in my_generator:
    print(item[0], '*', item[1], '=', item[2])
