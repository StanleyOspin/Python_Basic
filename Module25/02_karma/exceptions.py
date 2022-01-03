class KillError(Exception):
    minus_to_karma = 2

    def __init__(self):
        self.message = 'Убил комара, но он напал первым, минус {} к карме'.format(KillError.minus_to_karma)

    def __str__(self):
        return self.message


class DrunkError(Exception):
    minus_to_karma = 1

    def __init__(self):
        self.message = 'День начался вроде бы неплохо, но на всякий случай... все же выпил, минус {} к карме.'.format(
            DrunkError.minus_to_karma)

    def __str__(self):
        return self.message


class CarCrashError(Exception):
    minus_to_karma = 1

    def __init__(self):
        self.message = 'Полицейский приказал мне остановиться, и я въехал в столб, минус {}  карме.'.format(
            CarCrashError.minus_to_karma)

    def __str__(self):
        return self.message


class GluttonyError(Exception):
    minus_to_karma = 1

    def __init__(self):
        self.message = 'Иногда, если даже нельзя съесть прирожное, но очень хочется, то можно, минус {} к карме.'.format(
            GluttonyError.minus_to_karma)

    def __str__(self):
        return self.message


class DepressionError(Exception):
    minus_to_karma = 3

    def __init__(self):
        self.message = 'Депрессия! Давно не виделись! Проходи! Чай, кофе или сразу водочки? Минус {} к карме.'.format(
            DepressionError.minus_to_karma)

    def __str__(self):
        return self.message
