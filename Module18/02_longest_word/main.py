string = input('Введите строку: ').split()
print()
print('Самое длинное слово в строке: ', max(string, key=len))
print('Длина слова: ', len(max(string, key=len)), 'букв')
