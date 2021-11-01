def moves(n, x=1, y=3):
    if n == 1:
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n, x, y))
    else:
        moves(n - 1, x, 6 - x - y)
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n, x, y))
        moves(n - 1, 6 - x - y, y)


disc_number = int(input('Введите количество дисков: '))
moves(disc_number)
