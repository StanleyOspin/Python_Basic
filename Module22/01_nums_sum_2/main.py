import os

name = 'numbers.txt'
file_path = os.path.abspath('numbers.txt')

numbers_file = open(file_path, 'r')
numbers_list = numbers_file.read().split()
summa = sum([int(symbol) for symbol in numbers_list])
answer_file = open('answer.txt', 'w')
answer_file.write(str(summa))
numbers_file.close()
answer_file.close()
