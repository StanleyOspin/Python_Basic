class Warrior:
    def __init__(self, health, hit=20):
        self.health = health
        self.hit = hit

    def isattacked(self):
        self.health -= self.hit

    # TODO добавьте метод "удар"/"атака"|"бой" принимающий через параметр объект врага и уменьшающий значение его
    #  атрибута health

    def health_level(self):
        if self.health == 0:  # TODO получилось так: если значение сравнения Истина, то верни Истину, а если Ложно,
                              #  то верни Ложно. Чтобы избежать тавтологии просто верните значение сравнения без
                              #  дублирования возможных вариантов его значения
            return False
        else:
            return True
