n = int(input('Введите число: '))
divider = 1
while divider <= n:
    divider += 1
    if n % divider == 0:
        break
print('Наименьший делитель, отличный от единицы: ', divider)
