import os


def find_file(current_path, file_name, dir_list=[]):
    print('\nпереходим: ', current_path)

    for item in os.listdir(current_path):
        path = os.path.join(current_path, item)
        print('     смотрим', path)

        if item == file_name:
            dir_list.append(path)

        if os.path.isdir(path):
            result = find_file(path, file_name)

    else:
        result = None

    return dir_list


path = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))
file = 'main.py'

result = find_file(path, file)
if result:
    print('\nНайдены следующие пути: ')
    for i in result:
        print(i)

else:
    print('\nУказанного пути не существует')
