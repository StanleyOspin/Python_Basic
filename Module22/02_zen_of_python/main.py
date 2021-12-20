import os

file_path = os.path.abspath('zen.txt')

file = open(file_path, 'r')
string = file.read().split('.')

string.reverse()
print('\n'.join(string))

file.close()
print()
# version_2

file = open(file_path, 'r')
string = file.readlines()
string.reverse()

print(''.join(string))

file.close()
