shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
total_cost = 0
count = 0
detail = input('Название детали: ')

for item in shop:
        for part in item:
                if part == detail:
                        total_cost += item[1]
                        count += 1

print('\nКол-во деталей - ', count)
print('Общая стоимость - ', total_cost)



