def height_count(member):
    if member not in family_tree:
        return 0
    else:
        return 1 + height_count(family_tree[member])


quantity = int(input('Введите количество человек: '))
family_tree = dict()

for i in range(quantity - 1):
    child, parent = input('{0} пара: '.format(i + 1)).split()
    family_tree[child] = parent

height = dict()

for member in set(family_tree.keys()).union(set(family_tree.values())):
    height[member] = height_count(member)

print()
print('“Высота” каждого члена семьи: ', end='\n')

for k, v in sorted(height.items()):
    print(k, v)
