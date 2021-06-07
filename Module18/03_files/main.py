file = input('Название файла: ')
forbiden_symbols = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
if file[0] in forbiden_symbols:
    print('\nОшибка: название начинается на один из специальных символов')
elif not file.endswith(('.txt', '.docx')):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
