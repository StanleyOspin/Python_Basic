from parent_child import Parents, Child


parent = Parents('Вася', 35, children=[])
living_hours = 14
child_count = int(input('Сколько детей у {}? '.format(parent.parent_name[0:-1] + 'и')))


def child_input():
    child_name = input('Имя ребенка: ')
    child_age = int(input('Возраст ребенка: '))

    return child_name, child_age


children = [Child(*child_input()) for child in range(child_count)]

parent.children = children
parent.check_age()
parent.print_info()
for hour in range(living_hours):
    parent.child_make_calm()
    parent.child_feed()