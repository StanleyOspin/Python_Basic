friends_quantity = int(input('Кол-во друзей: '))
receipts_quantity = int(input('Долговых расписок: '))
receipts = []

for friend in range(1, friends_quantity + 1):
    receipts.append(list([friend, 0]))

for i in range(1, receipts_quantity + 1):
    print()
    print(i, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    receipts[to_whom - 1][1] += how_much
    receipts[from_whom - 1][1] -= how_much

print('\Баланс друзей: ')
for j in range(len(receipts)):
    print(receipts[j][0], ':', receipts[j][1])
