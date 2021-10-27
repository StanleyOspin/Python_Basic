def calculating_math_func(data):
    # TODO добавьте параметр cache={} и используйте его для хранения данных ("изменяемые" mutable объекты указанные в
    #  качестве значений по-умолчанию сохраняются между вызовами функции).
    #  Эта особенность питона считается "ловушкой", тут вы просто знакомитесь с ней, чтобы не попадаться в неё в будущем

    if data in factorials:
        result = factorials[data]

    else:
        result = max(factorials.values())

        for index in range(max(factorials.keys()) + 1, data + 1):
            result *= index
            factorials[index] = result

    result /= data ** 3

    result = result ** 10

    return result


factorials = {1: 1}  # TODO используйте для хранения параметр функции вместо глобальной переменной
number = int(input('Введите число: '))
while number != 0:
    result = calculating_math_func(number)
    print(result)
    number = int(input('Введите число: '))
