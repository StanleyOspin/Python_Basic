word = input('Введите слово: ')
word_list = list(word)
reversed_word = ''

for items in word_list[::-1]:
    reversed_word += items

if word == reversed_word:  # TODO достаточно так: word == word[::-1]
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
