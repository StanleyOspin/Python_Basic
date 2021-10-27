def simple_list(some_list, new_list):
    some_list = [new_list.append(item)
                 if isinstance(item, int) else simple_list(item, new_list)
                 for item in some_list]

    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_list = []
new_list = simple_list(nice_list, new_list)
print(new_list)


# TODO Другой вариант:
def flatten(a_list):
    result = []
    for e in a_list:
        if isinstance(e, int):
            result.append(e)
        else:
            result.extend(flatten(e))
    return result


nice_list = flatten(nice_list)

print(nice_list)
