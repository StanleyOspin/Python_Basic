def simple_list(some_list, new_list):
    some_list = [new_list.append(item)
                 if isinstance(item, int) else simple_list(item, new_list)
                 for item in some_list]

    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_list = []
new_list = simple_list(nice_list, new_list)
print(new_list)
