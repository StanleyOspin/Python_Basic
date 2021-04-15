list_1 = [1, 5, 3]
list_2 = [1, 5, 1, 5]
list_3 = [1, 3, 1, 5, 3, 3]

list_1.extend(list_2)
print('Кол-во цифр 5 при первом объединении: ', list_1.count(5))

for item in list_1:
    if item == 5:
        list_1.remove(item)

list_1.extend(list_3)
print('Кол-во цифр 3 при втором объединении: ', list_1.count(3))
print('Итоговый список: ', list_1)