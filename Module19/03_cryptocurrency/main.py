data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

keys = list()
values = list()

for key in data.keys():
    keys.append(key)

for value in data.values():
    values.append(value)

print('Список ключей словаря: ', keys)
print()
print('Список значений словаря: ', values)
print()

data['ETH']['total_diff'] = 100
print('В ETH добавлен новый элемент: ', data['ETH'])
print()

data['tokens'][0]['fst_token_info']['name'] = 'doge'
print('Внутри "fst_token_info" значение ключа "name" стало =', data['tokens'][0]['fst_token_info']['name'])
print()

for item in data['tokens']:
    data['ETH']['total_Out'] = item.pop('total_out')

print('Удалено "total_out" из tokens и присвоено его значение в "total_out" внутри "ETH":', data['ETH']['total_Out'])
print()

data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = False
print('Название ключа "price" изменено на "total_price" в "sec_token_info": ', data['tokens'][1]['sec_token_info'])
