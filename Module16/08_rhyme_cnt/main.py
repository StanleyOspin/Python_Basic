humans = list(range(1, int(input('Кол-во человек: ')) + 1))

number = int(input('Какое число в считалке? '))

print('Значит, выбывает каждый', number, 'человек')

count = 0

while len(humans) > 1:

    print('\nТекущий круг людей:', humans)

    print('Начало отсчета с номера:', humans[count])

    delete = (count + number - 1) % len(humans)

    if humans[delete] == humans[-1]:

        count = 0

    else:

        count = delete

    print('Выбывает человек под номером: ', humans[delete])

    humans.remove(humans[delete])

print('\nОстался человек под номером', humans[0])
