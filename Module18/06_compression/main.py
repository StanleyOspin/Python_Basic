string = input('Введите строку: ')
coded_string = ''

for i in string:
    if len(coded_string) == 0:
        coded_string = i + '1'
    else:
        if i == coded_string[-2]:
            coded_string = '{}{}'.format(coded_string[:-1], int(coded_string[-1]) + 1)
        else:
            coded_string = '{}{}{}'.format(coded_string, i, '1')

print('\nЗакодированная строка: ', coded_string)

