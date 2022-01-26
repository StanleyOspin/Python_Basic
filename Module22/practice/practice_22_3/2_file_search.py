import os


def create_path(directory, file_name, dir_list=[]):
    for dirs, folder, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(dirs, file)
                dir_list.append(file_path)
    return dir_list


# disk = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))
disk = 'D:'
# name = 'main.py'
name = 'group_1.txt'
result = create_path(disk, name)
if result:
    print('\Найдены следующие файлы: ')
    for file in result:
        print(file)
else:
    print('Такого файла здесь нет')

# file = open(result[1], 'r', encoding='utf-8')
data = open(result[0], 'r', encoding='utf-8')
sym_count = []
for i_line in data:
    print(i_line, end='')
    sym_count.append(str(len(i_line)))
print()
sym_count_str = '\n'.join(sym_count)
data.close()

counts_file = open('sym_count.txt', 'w', encoding='utf-8')
counts_file.write(sym_count_str)
counts_file.close()