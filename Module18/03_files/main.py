file = input('Название файла: ')
if file.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')',)) == True:
    print('\Ошибка: название начинается на один из специальных символов')
elif not file.endswith(('.txt', '.docx')):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
