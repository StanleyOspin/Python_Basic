import os


def foo(some_path):
    if os.path.isfile(some_path):
        return print('\nЭто файл', '\nРазмер файла: ', os.stat(some_path).st_size)

    elif os.path.isdir(some_path):
        return print('\n Это папка')

    elif os.path.islink(some_path):
        return print('\nЭто ссылка')

    elif not os.path.exists(path):
        return print('Указанного пути не существует')


path = os.path.abspath(os.path.join('..', 'practice_22_1', '01_sysadmin.py'))
foo(path)
