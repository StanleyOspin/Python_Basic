import os


def doc_saving(string, path, name):
    for address, dirs, files in os.walk(path):
        if not os.path.exists(path):
            return None
        else:
            for file in files:
                file_path = os.path.join(address, name)

                if os.path.exists(file_path):
                    request_rewrite = input('\nВы действительно хотите перезаписать файл? yes/no ').lower()
                    if request_rewrite == 'yes':
                        file = open(file_path, 'w', encoding='utf-8')
                        file.write(string)
                        file.close()
                        print('Файл успешно перезаписан!')
                        return file_path
                    else:

                        print('Перезапись файла отменена')
                        return file_path

                else:
                    file = open(file_path, 'w', encoding='utf-8')
                    file.write(string)
                    file.close()
                    print('\nФайл успешно сохранён!')
                    return file_path


text = input('Введите строку: ')
print()
user_input = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
user_input = '/'.join(map(str, user_input))
user_path = os.path.join(user_input)
print()
file_name = input('Введите имя файла: ')
result = doc_saving(text, user_path, file_name)

if result:
    print()
    print('Содержимое файла: ')
    saved_file = open(result, 'r')
    print(saved_file.read())
    saved_file.close()
else:
    print('Указанный путь не существует')
