import random

team_1 = [round(random.uniform(5, 10), 2) for i_team in range(20)]
print('Первая команда:', team_1)

team_2 = [round(random.uniform(5, 10), 2) for i_team in range(20)]
print('Вторая команда:', team_2)

winners = [team_1[i_team] if team_1[i_team] > team_2[i_team] else team_2[i_team]
           for i_team in range(20)]
print('\nПобедители тура:', winners)