goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key, value in goods.items():
    item_quantity = 0
    item_costs = 0
    item_total_quantity = 0
    item_total_costs = 0
    for item in store[value]:
        item_quantity = 0
        item_costs = 0
        item_quantity += item['quantity']
        item_costs += item['price']
        item_total_quantity += item_quantity
        item_total_costs += item_quantity * item_costs
    print('{0} - {1} шт, стоимость {2} руб'.format(key, item_total_quantity, item_total_costs))
