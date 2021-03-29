k = int(input('Сдвиг: '))
number_list = [1, 2, 3, 4, 5]
print('Изначальный список: ', number_list)

while True:
    if k == 0:
        break
    else:
        new_list = number_list[k:] + number_list[:k]
        print('Сдвинутый список: ', new_list)
    k = int(input('Сдвиг: '))
