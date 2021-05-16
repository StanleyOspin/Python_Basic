def check_letter(string, letter):
    row = 'аоеёиуыэюя'
    if letter in row:
        return letter


text = input('Введите текст: ')
vowels = [letter for letter in text if check_letter(text, letter)]

print('\nСписок гласных букв: ', vowels)
print('Длина списка: ', len(vowels))

