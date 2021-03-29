numbers_list = [1, 4, -3, 0, 10]
print('Изначальный список: ', numbers_list)
sorted = True

while sorted:
    sorted = False
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] > numbers_list[i + 1]:
            numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]

            sorted = True

print()
print('Отсортированный список: ', numbers_list)
