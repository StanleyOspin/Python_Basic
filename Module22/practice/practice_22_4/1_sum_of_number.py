import os


def create_path(directory, file_name):
    for dirs, folder, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(dirs, file)
                return file_path

    else:
        return None


path = 'D:'
file = 'numbers.txt'


#path = 'D:'

#file = 'numbers.txt'

file_path = create_path(path, file)
file_path = open(file_path, 'r',  encoding='utf-8')
answer_file = open('answer.txt', 'w', encoding='utf-8')
summa = 0
if file_path:

    for i_line in file_path:
        summa += int(i_line)
    answer_file.write(str(summa))
    answer_file.close()
    file_path.close()
else:
    print('Такого файла здесь нет')