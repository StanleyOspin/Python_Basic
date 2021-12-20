from warrior import Warrior
import random

warrior_1 = Warrior(100)
warrior_2 = Warrior(100)

while True:

    who_is_attack = random.randint(1, 2)
    if who_is_attack == 1:
        warrior_2.isattacked()
        print('Атаковал {} , у {} осталось {} единиц здоровья'.format('воин 1 ', 'воина 2', warrior_2.health))
        if not Warrior.health_level(warrior_2):
            print('Игра окончена, победил {}'.format('воин 1 '))
            break

    else:
        warrior_1.isattacked()
        print('Атаковал {} , у {} осталось {} единиц здоровья'.format('воин 2 ', 'воина 1', warrior_1.health))
        if not Warrior.health_level(warrior_1):
            print('Игра окончена, победил {}'.format('воин 2'))
            break
