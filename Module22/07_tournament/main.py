import os

first_tour = os.path.abspath('first_tour.txt')
second_tour = os.path.abspath('path_second_tour.txt')

file_first_tour = open(first_tour, 'r', encoding='utf-8')
k = int(file_first_tour.read(3))
players_dict = {}

for string in file_first_tour:
    string = string.split()

    if int(string[2]) > k:
        players_dict[string[1].replace(string[1], string[1][0] + '.') + string[0]] = int(string[2])
results_sorted = ((key, players_dict[key]) for key in sorted(players_dict, key=players_dict.get, reverse=True))
second_tour_players_number = str(len(players_dict))
file_first_tour.close()

file_second_tour = open(second_tour, 'a', encoding='utf-8')

numbering = 0
file_second_tour.write(second_tour_players_number + '\n')
for item in results_sorted:
    numbering += 1
    file_second_tour.write(str(numbering) + ') ' + item[0] + ' ' + str(item[1]) + '\n')

file_second_tour.close()
