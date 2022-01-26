import os

folder = 'access'
file = 'admin.bat'
print('\nАбсолютный путь до файла: ', os.path.abspath(os.path.join(folder, file)))
print()
print('Относительный путь до файла: ', os.path.abspath(os.path.join('..', '..', '..', folder, file)))