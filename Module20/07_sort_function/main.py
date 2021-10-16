def sorting(some_tuple):
    for i in some_tuple:
        if not isinstance(i, int):
            return original_tuple
    sorted_tuple = tuple(sorted(original_tuple))  # TODO Забыли return, сейчас возвращается None


# original_tuple = [9, 8, 7, 6, 5.5, 4, 3, 2, 1]
original_tuple = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sorting(original_tuple))
