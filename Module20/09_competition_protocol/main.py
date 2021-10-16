quantity = int(input('Сколько записей вносится в протокол? '))
results = {}

for i in range(1, quantity + 1):
    points, name = input('{0} запись: '.format(i)).split()
    points = int(points)
    if results.get(name, 0) == 0 or points > results[name][0]:
        results[name] = [points, i]

results = [(key, value[0], value[1]) for key, value in results.items()]
results_sorted = sorted(results, key=lambda x: (-x[1], x[2]))

print('\nИтоги соревнований:')
for i in range(3):
    print('{0} место. {1} ({2}) '.format(i + 1, results_sorted[i][0], results_sorted[i][1]))
