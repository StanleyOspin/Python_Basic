class Warrior:
    def __init__(self, health, hit=20):
        self.health = health
        self.hit = hit

    def isattacked(self):
        self.health -= self.hit

    def health_level(self):
        if self.health == 0:
            return False
        else:
            return True
