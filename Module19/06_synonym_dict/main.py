def check_synonym_dict(synonym_dict, inverted):
    word = input('\nВведите слово: ').title()
    if word in synonym_dict:
        synonym = synonym_dict[word]
        print('Синоним: ', synonym)
    elif word in inverted:
        synonym = inverted[word]
        print('Синоним: ', synonym)
    else:
        print('Такого слова в словаре нет.')
        check_synonym_dict(synonym_dict, inverted)


couples_quantity = int(input('Введите количество пар слов: '))
synonym_dict = dict()

for i in range(couples_quantity):
    couple = input('{0} пара: '.format(i + 1)).split(' - ')
    synonym_dict.setdefault(couple[0], couple[1])

inverted = {value: key for key, value in synonym_dict.items()}

check_synonym_dict(synonym_dict, inverted)
