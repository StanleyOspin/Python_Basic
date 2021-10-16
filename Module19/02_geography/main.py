database = dict()
countries = int(input('Кол-во стран: '))

for i in range(countries):
    value = input('{0} страна: '.format(i + 1)).split()
    for town in value[1:]:
        database[town] = value[0]

for i in range(3):
    city = input('\n{0} город: '.format(i + 1))
    country = database.get(city)
    if country:
        print('Город {0} расположен в стране {1}'.format(city, country))
    else:
        print('По городу {0} данных нет.'.format(city))


