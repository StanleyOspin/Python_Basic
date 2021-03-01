year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))
print('\nГода от', year_1, 'до', year_2, 'с тремя одинаковыми цифрами: ')
for year in range(year_1, year_2 + 1):
    figure = year
    number_1 = figure % 10
    figure //= 10
    number_2 = figure % 10
    figure //= 10
    number_3 = figure % 10
    figure //= 10
    number_4 = figure % 10

    if number_1 == number_2 and number_2 == number_3:
        print(year)
    elif number_1 == number_3 and number_3 == number_4:
        print(year)
    elif number_2 == number_3 and number_3 == number_4:
        print(year)
    elif number_1 == number_4 and number_2 == number_4:
        print(year)








