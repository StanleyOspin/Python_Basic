films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_films = []
find_films = input('Какой фильм ищем? ')

while find_films != 'end':
    count = 0
    for index in range(len(films)):

        if find_films == films[index]:
            favorite_films.append(find_films)
        else:
            count += 1
    if count > index:
        print('\n Ошибка. Рецензия на фильм', find_films, 'отсутствует')

    find_films = input('Какой фильм ищем? ')

print('\nНа эти фильмы рецензии вы можете почитать:', end=' ')

for film in favorite_films:
    print(film, end=' ')
