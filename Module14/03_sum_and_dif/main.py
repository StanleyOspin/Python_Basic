def summa(n):
    summa = 0
    while n > 0:
        digit = n % 10
        summa += digit
        n //= 10
    return summa


def count(n):
    count = 0
    while n > 0:
        digit = n % 10
        count += 1
        n //= 10
    return count


n = int(input('Введите число: '))
summ = summa(n)
number_count = count(n)
print('\nСумма цифр:', summ)
print('Количество цифр в числе:', number_count)
print('Разность суммы и количества цифр:', abs(summ - number_count))
