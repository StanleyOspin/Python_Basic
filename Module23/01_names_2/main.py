import os

symbols_sum = 0
line_count = 0
people_file_address = os.path.abspath('people.txt')
errors_file_address = os.path.abspath('errors.log')
with open(people_file_address, 'r', encoding='utf-8') as people_file:
    for i_line in people_file:
        try:
            line_count += 1
            i_line = ''.join([symbol for symbol in i_line if symbol.isalnum()])
            symbols_sum += len(i_line)
            if len(i_line) < 3:
            # TODO Обычно "защищают" некий неизвестный код, от которого можно ждать "всякого плохого", например некую
            #  импортированную функцию.
            #  Создайте функцию "валидации имени" и выбрасывайте в ней исключение, а тут, в цикле вызывайте саму функцию
            #  валидации (валидация - проверка корректности данных)
                raise BaseException
                # TODO используйте более конкретный класс исключения, например ValueError.
                #  В любом случае, базовый класс всех простых исключений это Exception, а BaseException это "внутренности"
                #  реализации и обычно не используется
        except BaseException:
            with open(errors_file_address, 'a', encoding='utf-8') as errors_file:
                errors_file.write('BaseException: в строке {0} меньше 3-х символов'.format(line_count) + '\n')

    print('Сумма всех символов в файле: ', symbols_sum)
