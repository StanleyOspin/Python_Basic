import os

file_path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))

file = open(file_path, 'r')
string = file.read()

symbol_count = [symbol.lower() for symbol in list(string) if symbol.isalpha()]
print('Количество букв: ', len(symbol_count))
print()
words_count = len([word for word in string.split()])
print('Количество слов: ', words_count)
print()
line_count = len([line for line in string.split('.')])
print('Количество строк: ', line_count)
print()
symbol_dict = dict.fromkeys(symbol_count)

for item in symbol_dict:
    symbol_dict[item] = symbol_count.count(item)
print('Наименьшее количество раз встречается буква', min(symbol_dict, key=symbol_dict.get))
file.close()
