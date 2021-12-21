import os

PATH_TO_REGISTRATIONS = os.path.abspath('registrations.txt')
PATH_TO_GOOD_LOG = os.path.abspath('registrations_good.log')
PATH_TO_BAD_LOG = os.path.abspath('registrations_bad.log')
#Exceptions:

def validation_check(data_list):
    if len(data_list) < 3:
        raise IndexError('НЕ присутствуют все три поля')

    elif not data_list[0].isalpha():
        raise NameError('поле имени содержит НЕ только буквы')

    elif data_list[1].count('@') != 1 and data_list[1].count('.') != 1:
        raise SyntaxError('поле емейл НЕ содержит @ и .(точку)')

    elif int(data_list[2]) < 10 or int(data_list[2]) > 99:
        raise ValueError('поле возраст НЕ является числом от 10 до 99')

    else:
        return ' '.join((data_list[0], data_list[1], data_list[2]))



count = 0

with open(PATH_TO_REGISTRATIONS, 'r', encoding='utf-8') as registrations_file,\
     open(PATH_TO_GOOD_LOG, 'w', encoding='utf-8') as good_log_file,\
     open(PATH_TO_BAD_LOG, 'w', encoding='utf-8') as bad_log_file:


    for i_line in registrations_file:
        count += 1
        data_list = i_line.split()
        try:
            string = validation_check(data_list)
            good_log_file.write(string + '\n')

        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            error_message = f'{i_line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
            bad_log_file.write(error_message + '\n')



