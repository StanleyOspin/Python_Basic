class Warrior:
    def __init__(self, health, hit=20):
        self.health = health
        self.hit = hit

    def fight(self, warrior):
        self.health -= self.hit
        # TODO сейчас для бойца "бой" уменьшает ему самому здоровье, но по заданию предполагался метод для нанесения
        #  урона врагу:
        # def fight(self, enemy):
        #     enemy.health -= self.hit

    def health_level(self):
        if self.health == 0:
            return True
        # TODO если self.health не равно 0, то вернётся None, что не совсем корректно, но если перенести сравнение в
        #  return, то будут возвращаться только булевы значения, что и ожидается от метода.
        #  Вот о чём был прошлый комментарий:
        # def health_level(self):
        #     return self.health == 0
