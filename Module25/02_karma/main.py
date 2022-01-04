from random import randint
from exceptions import *
from buddhist import Buddhist

buddhist = Buddhist()


def one_day():
    dice = randint(1, 10)
    if dice == 1:
        raise KillError
    elif dice == 2:
        raise DrunkError
    elif dice == 3:
        raise CarCrashError
    elif dice == 4:
        raise GluttonyError
    elif dice == 5:
        raise DepressionError
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

    except KillError:
        with open('karma_log', 'a', encoding='utf-8') as file:
            buddhist.set_karma(buddhist.get_karma() - KillError.minus_to_karma)
            day = buddhist.get_day()
            day += 1
            buddhist.set_day(day)
            file.write('День: {}.  Убил комара, но он напал первым, минус {} к карме' \
                       .format(buddhist.get_day(), KillError.minus_to_karma) + '\n')

    except DrunkError:
        with open('karma_log', 'a', encoding='utf-8') as file:
            buddhist.set_karma(buddhist.get_karma() - DrunkError.minus_to_karma)
            day = buddhist.get_day()
            day += 1
            buddhist.set_day(day)
            file.write('День: {}. День начался вроде бы неплохо, но на всякий случай... все же выпил, минус {} к карме.' \
                       .format(buddhist.get_day(), DrunkError.minus_to_karma) + '\n')

    except  CarCrashError:
        with open('karma_log', 'a', encoding='utf-8') as file:
            buddhist.set_karma(buddhist.get_karma() - CarCrashError.minus_to_karma)
            day = buddhist.get_day()
            day += 1
            buddhist.set_day(day)
            file.write('День: {}. Полицейский приказал мне остановиться, и я въехал в столб, минус {}  карме.' \
                       .format(buddhist.get_day(), CarCrashError.minus_to_karma) + '\n')
    except GluttonyError:
        with open('karma_log', 'a', encoding='utf-8') as file:
            buddhist.set_karma(buddhist.get_karma() - GluttonyError.minus_to_karma)
            day = buddhist.get_day()
            day += 1
            buddhist.set_day(day)
            file.write(
                'День: {}. Иногда, если даже нельзя съесть прирожное, но очень хочется, то можно, минус {} к карме.' \
                .format(buddhist.get_day(), GluttonyError.minus_to_karma) + '\n')

    except DepressionError:
        with open('karma_log', 'a', encoding='utf-8') as file:
            buddhist.set_karma(buddhist.get_karma() - DepressionError.minus_to_karma)
            day = buddhist.get_day()
            day += 1
            buddhist.set_day(day)
            file.write('День: {}. Депрессия! Давно не виделись! Проходи! Чай, кофе или сразу водочки? Минус {} к карме.' \
                       .format(buddhist.get_day(), DepressionError.minus_to_karma) + '\n')
