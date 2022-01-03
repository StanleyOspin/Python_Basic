from random import randint, choice
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

    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError):

        with open('karma_log', 'a', encoding='utf-8') as file:
            if KillError:
                karma = buddhist.set_karma(buddhist.get_karma() - KillError.minus_to_karma)
                file.write('День ' + str(buddhist.get_day()) + '\n') #не могу понять как вывести сообщение из класса exception
            elif DrunkError:
                karma = buddhist.set_karma(buddhist.get_karma() - DrunkError.minus_to_karma)
                file.write('День ' + str(buddhist.get_day()) + '\n')#не могу понять как вывести сообщение из класса exception
            elif CarCrashError:
                karma = buddhist.set_karma(buddhist.get_karma() - CarCrashError.minus_to_karma)
                file.write('День ' + str(buddhist.get_day()) + '\n')#не могу понять как вывести сообщение из класса exception
            elif GluttonyError:
                karma = buddhist.set_karma(buddhist.get_karma() - GluttonyError.minus_to_karma)
                file.write('День ' + str(buddhist.get_day()) + '\n')#не могу понять как вывести сообщение из класса exception
            elif DepressionError:
                karma = buddhist.set_karma(buddhist.get_karma() - DepressionError.minus_to_karma)
                file.write('День ' + str(buddhist.get_day()) + '\n')#не могу понять как вывести сообщение из класса exception
