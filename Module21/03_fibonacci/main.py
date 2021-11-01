def fibonacci(number_position):
    if number_position in (1, 2):
        return 1
    return fibonacci(number_position - 1) + fibonacci(number_position - 2)


number_position = int(input('Введите позицию числа в ряде Фибоначчи: '))
fibonacci_number = fibonacci(number_position)
print('Число: ', fibonacci_number)
