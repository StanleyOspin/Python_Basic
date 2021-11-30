import os


def validation_check(i_line):
    if len(i_line) < 3:
        raise IndexError

    elif not i_line[0].isalpha():
        raise NameError

    elif i_line[1].count('@') != 1 and i_line[1].count('.') != 1:
        raise SyntaxError

    elif int(i_line[2]) < 10 or int(i_line[2]) > 99:
        raise ValueError

    else:
        return ' '.join((i_line[0], i_line[1], i_line[2]))


path_to_registrations = os.path.abspath('registrations.txt')
path_to_good_log = os.path.abspath('registrations_good.log')
path_to_bad_log = os.path.abspath('registrations_bad.log')
count = 0

with open(path_to_registrations, 'r', encoding='utf-8') as registrations_file:
    for i_line in registrations_file:
        count += 1
        i_line = i_line.split()
        try:
            string = validation_check(i_line)

            with open(path_to_good_log, 'a', encoding='utf-8') as good_log_file:
                good_log_file.write(string + '\n')

        except IndexError:
            with open(path_to_bad_log, 'a', encoding='utf-8') as good_log_file:
                good_log_file.write('IndexError: в строке {0} не хватает данных'.format(count) + '\n')

        except NameError:
            with open(path_to_bad_log, 'a', encoding='utf-8') as good_log_file:
                good_log_file.write('NameError: в строке {0} поле "Имя" содержит не только буквы'.format(count) + '\n')

        except SyntaxError:
            with open(path_to_bad_log, 'a', encoding='utf-8') as good_log_file:
                good_log_file.write(
                    'SyntaxError: в строке {0} некорректно введен элетронный адрес'.format(count) + '\n')

        except ValueError:
            with open(path_to_bad_log, 'a', encoding='utf-8') as good_log_file:
                good_log_file.write('ValueError: в строке {0} не правильно введен возраст'.format(count) + '\n')
