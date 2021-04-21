# way_1
num_list_1 = []

for i in range(3):
    print('Число', i + 1, end=' ')
    number = int(input())
    num_list_1.append(number)

num_list_2 = []
print()

for j in range(7):
    print('Число', j + 1, end=' ')
    figure = int(input())
    num_list_2.append(figure)

num_list_1.extend(num_list_2)

for item in num_list_1:
    while num_list_1.count(item) > 1:
        num_list_1.remove(item)

print('\n Новый первый список с уникальными элементами: ', num_list_1)

# way_2
num_list_1 = []

for i in range(3):
    print('Число', i + 1, end=' ')
    number = int(input())
    num_list_1.append(number)

num_list_2 = []
print()

for j in range(7):
    print('Число', j + 1, end=' ')
    figure = int(input())
    num_list_2.append(figure)

num_list_1.extend(num_list_2)
unique_numbers = list(set(num_list_1))
print('\n Новый первый список с уникальными элементами: ', num_list_1)
