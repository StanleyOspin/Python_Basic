def years(year_1, year_2):
    for year in range(year_1, year_2 + 1):

        count = 0

        check_number = year % 10

        number = year

        while number > 0:

            next_number = number % 10

            if check_number == next_number:
                count += 1

            number = number // 10

        if count == 3:  # по-хорошему нам нужны только 3 числа одинаковых, а 4 уже перебор - поправил
            print(year)


year_1 = int(input('Введите первый год: '))

year_2 = int(input('Введите второй год: '))

print('\nГода от', year_1, 'до', year_2, 'с тремя одинаковыми цифрами: ')

years(year_1, year_2)
