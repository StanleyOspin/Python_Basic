def is_digit(ip):
    for i in ip:
        if not i.isdigit():
            return print(i, '- не целое число')
        elif int(i) > 255:
            return print(i, 'превышает 255')
    else:
        return print('IP-адрес корректен')


ip = input('Введите IP: ').split('.')

if len(ip) != 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    is_digit(ip)
