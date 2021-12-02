import os


def caesar_cipher(string_list):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    step = 0
    cipher_text = ''
    cipher_list = []

    for string in string_list:
        step += 1

        for symbol in string:
            current_place = alphabet.find(symbol)
            cipher = current_place + step

            if symbol in alphabet:
                cipher_text += alphabet[cipher]


            else:
                cipher_text += symbol

    cipher_list.append(cipher_text)

    return cipher_list


path_text = os.path.abspath('text.txt')
path_cipher_text = os.path.abspath('cipher_text.txt')
file_text = open(path_text, 'r')
data_list = file_text.readlines()
file_text = open(path_text, 'r')
print('Содержимое файла text.txt:')
print(file_text.read())

file_text.close()

cipher_text = caesar_cipher(data_list)

file_cipher_text = open(path_cipher_text, 'w')

for i in cipher_text:
    file_cipher_text.write(i)
    file_cipher_text.close()
print()
print('Содержимое файла cipher_text.txt:')
file_cipher_text = open(path_cipher_text, 'r')
print(file_cipher_text.read())
file_cipher_text.close()
