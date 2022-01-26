import os


def create_path(directory, file_name):
    for dirs, folder, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(dirs, file)
                return file_path

    else:
        return None


disk = 'D:'
name = 'group_1.txt'
second_name = 'group_2.txt'
file_path_1 = create_path(disk, name)
file_path_2 = create_path(disk, second_name)
file_path_1 = open(file_path_1, 'r', encoding='UTF8')
file_path_2 = open(file_path_2, 'r', encoding='UTF8')


def summa(path):
    summa = 0

    for i_line in path:
        info = i_line.split()
        summa += int(info[2])

    return summa


def difference(path):
    difference = 0
    points = []

    for i_line in path:
        info = i_line.split()
        points.append(int(info[2]))

    for i in points:
        difference = max(points) - i

    return difference


def composing(path):
    composing = 1
    for i_line in path:
        info = i_line.split()
        composing *= int(info[2])
    return composing


summa = summa(file_path_1)
difference = difference(file_path_1)
composing = composing(file_path_2)
print('Сумма очков первой группы: ', summa)
print('Разность очков первой группы: ', difference)
print('Произведение очков второй группы: ', composing)
file_path_1.close()
file_path_2.close()
