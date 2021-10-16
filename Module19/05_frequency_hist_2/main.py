def check_frecuency(string):
    symbol_dict = dict()
    for symbol in string:
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    return symbol_dict


def inverted_dict(symbol_dict):
    inverted_dict = dict()
    for key, value in symbol_dict.items():
        inverted_dict.setdefault(value, []).append(key)
    return inverted_dict


def printuot(dicts):
    for item in sorted(dicts.keys()):
        print(item, ':', dicts[item])


text = input('Введите текст: ')
symbol_dict = check_frecuency(text)
inverted = inverted_dict(symbol_dict)

print('Оригинальный словарь частот: ', end='\n')
for key, value in sorted(symbol_dict.items()):
    print(key, ':', value)

print()

print('Инвертированный словарь частот: ', end='\n')
for key, value in sorted(inverted.items()):
    print(key, ':', value)
