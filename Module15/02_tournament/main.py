# version_1
names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
index_list = []

for i in range(len(names)):
    if i % 2 == 0:
        index_list.append(names[i])

for name in index_list:
    print(name, end=' ')

# version_2
names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

print(names[::2])