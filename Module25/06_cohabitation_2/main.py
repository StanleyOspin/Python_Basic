from house import House
from husband import Husband
from wife import Wife
from baby import Baby
from cat import Cat
from familymember import FamilyMember

family = [Husband('Иван Иваныч', 30), Wife('Мария Петровна', 30), Baby('Саша', 30),
          Cat('Кот Васька', 30), Cat('Кот Барсик', 30), Cat('Кот Пушок', 30)]
eaten = 0
earned = 0
fur_coats = 0

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
        eaten += member.get_eaten()
        if isinstance(member, Husband):
            earned += member.get_earned()
            print(earned)
        elif isinstance(member, Wife):
            fur_coats += member.get_fur_coats()
print()
print(f'Еды съедено: {eaten}\nДенег заработано: {earned}\nШуб куплено: {fur_coats}')
