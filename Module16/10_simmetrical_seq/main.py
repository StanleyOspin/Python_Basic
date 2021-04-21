number_quantity = int(input('Кол-во чисел: '))
numbers_list = []

for element in range(number_quantity):
    number = int(input('Число: '))
    numbers_list.append(number)

print('\nПоследовательность: ', end='')

for number in numbers_list:
    print(number, end='')
print()

for i in range(len(numbers_list)):
    if numbers_list[i:] == numbers_list[i:][::-1]:
        print('Нужно приписать чисел: ', i)
        break

print('Сами числа: ', end='')
for number in numbers_list[:i][::-1]:
    print(number, end='')
