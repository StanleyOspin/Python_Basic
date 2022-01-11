from random import randint, choice
from exceptions import *
from buddhist import Buddhist

buddhist = Buddhist()


def one_day():
    exceptions = [KillError('Убил комара, но он напал первым, минус 10 к карме.'),
                  DrunkError('День начался вроде бы неплохо, но на всякий случай... все же выпил, минус 5 к карме.'),
                  CarCrashError('Полицейский приказал мне остановиться, и я въехал в столб, минус 5  карме.'),
                  GluttonyError(
                      'Иногда, если даже нельзя съесть пирожное, но очень хочется, то можно, минус 5 к карме.'),
                  DepressionError(
                      'Депрессия! Давно не виделись! Проходи! Чай, кофе или сразу водочки? Минус 15 к карме.')]
    r_choice = choice(exceptions)
    dice = randint(1, 10)
    if dice == 9:
        raise r_choice
    else:
        return randint(1, 7)


while True:

    try:
        karma = buddhist.get_karma()
        karma += one_day()
        buddhist.set_karma(karma)
        day = buddhist.get_day()
        day += 1
        buddhist.set_day(day)

        if buddhist.get_karma() >= 500:
            print('Просветеление наступило на {} день'.format(buddhist.get_day()))
            break

    except (KillError, DrunkError, CarCrashError, GluttonyError,
            DepressionError) as exc:

        with open('karma_log', 'a', encoding='utf-8') as file:
            buddhist.set_karma(buddhist.get_karma() - KillError.minus_to_karma)
            day = buddhist.get_day()
            day += 1
            buddhist.set_day(day)
            error_message = f'День: {buddhist.get_day()}. {exc.__class__.__name__} - {exc}'

            file.write(error_message + '\n')
