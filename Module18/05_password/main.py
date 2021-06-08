password = input('Придумайте пароль: ')
upper = 0
digit = 0

for element in password:
    if element.isupper() == True:  # TODO достаточно if element.isupper():
        upper += 1
    elif element.isdigit() == True:  # TODO Аналогично предыдущему
        digit += 1

if len(password) >= 8 and upper > 0 and digit >= 3:
    print('\nЭто надёжный пароль!')
else:
    print('\nПароль ненадёжный. Попробуйте ещё раз.')
