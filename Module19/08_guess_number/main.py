max_number = int(input('Введите максимальное число: '))
possible_numbers = set(range(1, max_number + 1))
player_1 = input('\nНужное число есть среди вот этих чисел: ').lower()

while player_1 != 'помогите!':
    player_2 = input('\nОтвет Артёма: ').lower()
    if player_2 == 'да':
        guess_number = set(map(int, player_1.split()))
        possible_numbers.intersection_update(guess_number)
        if len(possible_numbers) == 1:
            break
        else:
            player_1 = input('\nНужное число есть среди вот этих чисел: ').lower()
    elif player_2 == 'нет':
        guess_number = set(map(int, player_1.split()))
        possible_numbers.difference_update(guess_number)
        if len(possible_numbers) == 1:
            break
        else:
            player_1 = input('\nНужное число есть среди вот этих чисел: ').lower()
    else:
        print('Ошибка ввода')

if len(possible_numbers) == 1:
    print('Угадал')
    print('Загаданное число ', possible_numbers)
else:
    print('\nАртём мог загадать следующие числа: ', end='')
    for i in sorted(possible_numbers):
        print(i, end=' ')
