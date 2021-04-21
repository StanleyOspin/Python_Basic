def is_free_place(guests):
    if len(guests) < 6:
        return True
    else:
        return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print('Сейчас на вечеринке', len(guests), 'человек:', guests)

while True:
    print()
    action = input('Гость пришел или ушел? ')
    if action == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    elif action == 'пришел':
        if is_free_place(guests):
            guest_name = input('Имя гостя: ')
            print('Привет,', guest_name)
            guests.append(guest_name)
            print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
        else:
            guest_name = input('Имя гостя: ')
            print('Прости,', guest_name, 'но мест нет.')
            print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    elif action == 'ушел':
        guest_name = input('Имя гостя: ')
        print('Пока,', guest_name)
        guests.remove(guest_name)
        print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
