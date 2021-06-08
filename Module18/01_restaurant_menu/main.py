string = input('Введите строку: ').split()
print('Самое длинное слово в строке: ', max(string, key=len))
print('Его длинна: ', len(max(string, key=len)), 'букв')
