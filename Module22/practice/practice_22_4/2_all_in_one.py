import os


def create_path(directory, file_name, path_list=[]):
    for dirs, folder, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(dirs, file)
                path_list.append(file_path)
    return path_list


path = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))
name = 'main.py'
file_pathes = create_path(path, name)

for path in file_pathes:
    file = open(path, 'r', encoding='utf-8')
    scripts_file = open('scripts.txt', 'a', encoding='utf-8')
    scripts_file.write(file.read() + '\n***********************************' + '\n')
    file.close()
    scripts_file.close()
