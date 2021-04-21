n = int(input('Кол-во коньков: '))
skates = []

for i in range(n):
    print('Размер', i + 1, 'пары:', end=' ')
    skate_size = int(input())
    skates.append(skate_size)

k = int(input('\nКол-во людей: '))
people = []

for j in range(k):
    print('Размер ноги', j + 1, 'человека:', end=' ')
    foot_size = int(input())
    people.append(foot_size)
count = 0

for i_people in people:
    for j_skates in range(len(skates)):
        if skates[j_skates] >= i_people:
            skates.remove(skates[j_skates])
            count += 1
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count)
