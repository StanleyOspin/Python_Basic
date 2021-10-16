# version_1
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [*map(tuple, (zip(original_list[::2], original_list[1::2])))]
print(new_list)

# version_2
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [tuple(item) for item in zip(original_list[::2], original_list[1::2])]
print(new_list)

# version_3
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_dict = dict()

for index, item in enumerate(original_list):
    if index % 2 == 0:
        numbers_dict[index] = item + 1

new_list = [(key, value) for key, value in numbers_dict.items()]

print(new_list)
