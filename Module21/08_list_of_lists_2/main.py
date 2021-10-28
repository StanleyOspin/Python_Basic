def simple_list(some_list):
    new_list = []
    some_list = [new_list.append(item)
                 if isinstance(item, int) else new_list.extend(simple_list(item))
                 for item in some_list]

    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_list = simple_list(nice_list)
print(new_list)


# Спасибо, принял к сведению. В своем коде тоже изменения внес.
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
