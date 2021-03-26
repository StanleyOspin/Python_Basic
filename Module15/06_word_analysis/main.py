word = input('Введите слово: ')
letters = list(word)
count = 0

for i in letters:
    repetitions = 0
    for j in letters:
        if i == j:
            repetitions += 1
    if repetitions > 1:
        count += 1

unique_letters = len(letters) - count
print('\nКоличество уникальных букв: ', unique_letters)
