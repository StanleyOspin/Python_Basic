n = str(input('Введите первое число: '))
n_1, n_2 = n.split('.')
n_1 = float(n_1[::-1])
count = 1
for i in n_2:
    count *= 10
n_2 = float(n_2[::-1]) / count
reversed_n =  n_1 + n_2



k = str(input('Введите второе число: '))
k_1, k_2 = k.split('.')
k_1 = float(k_1[::-1])
count = 1
for i in k_2:
    count *= 10
k_2 = float(k_2[::-1]) / count
reversed_k = k_1 + k_2
print('\nПервое число наоборот: ', reversed_n)
print('Второе число наоборот: ', reversed_k)
print('Сумма: ', reversed_n + reversed_k)

