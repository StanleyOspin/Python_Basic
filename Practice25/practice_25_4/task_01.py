class Unit:

    def __init__(self, hitpoints, damage=0):
        self.set_hitpoints(hitpoints)
        self.damage = damage

    def damaged(self):
        self.__hitpoints -= self.damage

    def __str__(self):
        return 'Cостояние здоровья {}'.format(self.__hitpoints)

    def get_hitpoints(self):
        return self.__hitpoints

    def set_hitpoints(self, hitpoints):
        self.__hitpoints = hitpoints


class Soldier(Unit):

    def __init__(self, hitpoints, damage):
        super().__init__(hitpoints)
        self.damage = damage

    def damaged(self):
        hitpoints = self.get_hitpoints()
        hitpoints -= self.damage
        self.set_hitpoints(hitpoints)


class Citizen(Unit):

    def __init__(self, hitpoints, damage):
        super().__init__(hitpoints)
        self.damage = damage

    def damaged(self):
        hitpoints = self.get_hitpoints()
        hitpoints -= self.damage * 2
        self.set_hitpoints(hitpoints)


soldier = Soldier(hitpoints=100, damage=10)
citizen = Citizen(hitpoints=100, damage=10)
for _ in range(3):
    soldier.damaged()
    citizen.damaged()

print(soldier)
print(citizen)
