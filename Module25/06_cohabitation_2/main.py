from house import House
from husband import Husband
from wife import Wife
from cat import Cat
from familymember import FamilyMember

family = [Husband('Иван Иваныч', 30), Wife('Мария Петровна', 30), Cat('Кот Васька', 30)]

home = House()
for member in family:
    member.settle_in_the_house(home)

for day in range(1, 366):
    print('=============== день {} ================'.format(day))
    print(home)
    home.act()
    for member in family:
        print(member)
        member.act()
