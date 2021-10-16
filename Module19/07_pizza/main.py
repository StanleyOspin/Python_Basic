orders_quantity = int(input('Введите кол-во заказов: '))
orders_dict = dict()
orders = dict()

for i in range(orders_quantity):
    name, item, count = input('{0} заказ: '.format(i + 1)).split()
    if name not in orders_dict:
        orders_dict.setdefault(name, {item: int(count)})
    else:
        if item in orders_dict[name]:
            orders_dict[name][item] += int(count)
        else:
            orders.setdefault(item, int(count))
            orders_dict[name].update(orders)
            orders.clear()
print()
for k, v in sorted(orders_dict.items()):
    print(k, ':')
    for k, v in sorted(v.items()):
        print(' ', k, ':', v)
