import os

try:
    file_ages_path = os.path.abspath('age.txt')
    file_ages = open(file_ages_path, 'r')
    age_list = file_ages.read().split()
    ages_dict = {}

    for item in age_list:

        if int(item) == 5:
            ages_dict[item] = 'sweet childhood'
        elif int(item) == 15:
            ages_dict[item] = 'youth has come'
        elif int(item) == 20:
            ages_dict[item] = 'you are getting adult'
        elif int(item) == 30:
            ages_dict[item] = 'you are became adult'
        elif int(item) == 40:
            ages_dict[item] = 'you are mature'
        elif int(item) == 50:
            ages_dict[item] = 'you started to grow old'
        elif int(item) == 60:
            ages_dict[item] = 'it is not so far to pension'
        elif int(item) == 70:
            ages_dict[item] = 'congratulations, you are retired already for 5 years'
        elif int(item) == 80:
            ages_dict[item] = 'sand began to pour out of you'
        elif int(item) == 90:
            ages_dict[item] = 'Wow!!! You are SUPERSTAR'


    file_result = open('result.txt', 'w')

    for key, value in ages_dict.items():
        file_result.write((key + '-' + value + '\n'))

    file_ages.close()
    file_result.close()

except IsADirectoryError:
    print('ожидался файл, но это директория.')
except FileExistsError:
    print('Файл {0} уже существует'.format(file_result))
