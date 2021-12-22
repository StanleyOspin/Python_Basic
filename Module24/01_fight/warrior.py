class Warrior:
    def __init__(self, health, hit=20):
        self.health = health
        self.hit = hit

    def fight(self, enemy):
        enemy.health -= self.hit

    def health_level(self):
        return self.health == 0
