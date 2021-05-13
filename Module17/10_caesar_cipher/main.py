def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(symbol) + shift) % 33] if symbol != ' ' else ' ') for symbol in string]
    new_string = ''
    for item in char_list:
        new_string += item
    return new_string


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

cipher_string = caesar_cipher(message, shift)

print('Зашифрованное сообщение:', cipher_string)
