string = input('Введите строку: ')
array = set()

for i in string:
    if i in array:
        array.remove(i)
    else:
        array.add(i)

if len(array) > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
