text = input('Введите текст: ')
vowels = [letter for letter in text
          if letter == 'а' or letter == 'о'
          or letter == 'е' or letter == 'ё' or letter == 'и'
          or letter == 'у' or letter == 'ы' or letter == 'э'
          or letter == 'ю' or letter == 'я']
print('\nСписок гласных букв: ', vowels)
print('Длина списка: ', len(vowels))
