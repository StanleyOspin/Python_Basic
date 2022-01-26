import os


def find_file(current_path, file_name):
    print('\nпереходим: ', current_path)

    for item in os.listdir(current_path):
        path = os.path.join(current_path, item)
        print('     смотрим', path)

        if item == file_name:
            return path

        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break

    else:
        result = None

    return result


path = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))

file = 'main.py'

file_path = find_file(path, file)
history_file = open('searh_history.txt', 'a', encoding='utf-8')

if file_path:
    print('\nАбсолютный путь к файлу: ', file_path)
    history_file.write(file_path)
    history_file.close()

else:
    print('Такого файла здесь нет')
