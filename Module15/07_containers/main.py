quantity = int(input('Кол-во контейнеров: '))
containers_list = []

for _ in range(quantity):
    mass = int(input('Введите вес контейнера: '))

    while True:
        if mass > 0 and mass < 200:
            break
        else:
            print('Ошибка. Вес контейнера должен быть больше 0, но не должен превышать 200 кг')
            mass = int(input('Введите вес контейнера: '))

    containers_list.append(mass)

print(containers_list)
print()
mass_new = int(input('Введите вес нового контейнера: '))
containers_list.append(mass_new)

for i in range(len(containers_list)):
    highest_value_index = i
    for j in range(i + 1, len(containers_list)):
        if containers_list[j] >= containers_list[highest_value_index]:
            highest_value_index = j
            containers_list[i], containers_list[highest_value_index] = containers_list[highest_value_index], containers_list[i]

print('Номер, куда встанет новый контейнер: ', containers_list.index(mass_new) + 1)