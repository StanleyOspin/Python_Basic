import os

file_path = os.path.abspath('text.txt')
file_text = open(file_path, 'r')
string = file_text.read()
string = ''.join(symbol.lower() for symbol in string if symbol.isalpha())

symbol_dict = {symbol: round(string.count(symbol) / len(string), 3) for symbol in sorted(list(string))}

sorted_tuple = ((item, symbol_dict[item]) for item in sorted(symbol_dict, key=symbol_dict.get, reverse=True))
file_text.close()

fle_analysis_path = os.path.abspath('analysis.txt')
file_analysis = open(fle_analysis_path, 'w')

for item in sorted_tuple:
    data = item[0] + ' ' + str(item[1]) + '\n'
    file_analysis.write(data)

file_analysis.close()
