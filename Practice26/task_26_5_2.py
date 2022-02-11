import os

summ = 0
path = os.path.abspath('numbers.txt')
with open(path, 'r') as file:
    symbol_list = (item.split() for item in file)

    for string in symbol_list:
        for symbol in string:
            if symbol.isdigit():
                summ += int(symbol)

    print(summ)
