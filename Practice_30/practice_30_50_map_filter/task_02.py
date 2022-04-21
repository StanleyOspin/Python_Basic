from typing import List

string: List[str] = list(filter(lambda symbol: symbol.islower(), filter(lambda symbol: symbol.isalpha, (input('Введите строку: ')))))

print(string)