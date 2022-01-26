BRUCE_WILLIS = 42

try:

    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except ValueError:
    print('невозможно преобразовать к числу')
except IndexError:
    print('выход за границы списка')

except NameError:
    print('переменной с таким именем не существует')
