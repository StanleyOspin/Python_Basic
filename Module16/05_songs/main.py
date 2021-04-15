violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

my_list = []
quantity = int(input('Сколько песен выбрать? '))

for element in range(quantity):
    print('\nНазвание', element + 1, 'песни: ', end='')
    song = input()
    my_list.append(song)
    play_time = 0

for i in range(len(my_list)):
    for j in range(len(violator_songs)):
        if my_list[i] == violator_songs[j][0]:
            play_time += violator_songs[j][1]

print('\nОбщее время звучания песен:', round(play_time, 2), 'минут')
