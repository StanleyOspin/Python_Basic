def identity_chek(string_1, string_2):
    k = 1
    possible = False
    for i in range(len(string_2)):
        string_2 = string_2[-1] + string_2[:-1]
        if string_1 == string_2:
            possible = True
            return print('Первая строка получается из второй со сдвигом', k)
        else:
            k += 1
    if not possible:
        return print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')

if string_1 == string_2:
    print('Строки идентичны!')
elif len(string_1) != len(string_2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    identity_chek(string_1, string_2)
