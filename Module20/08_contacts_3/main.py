phonebook = {}
while True:
    action = int(input('1 - Создать контакт\t2 - Поиск в контактах\t3 - Выход\n'))
    if action == 1:
        name = input('Имя: ').title()
        surname = input('Фамилия: ').title()
        name_surname = name, surname
        if name_surname in phonebook:
            print('Этот контакт уже существует')
            changes = int(input('1 - Добавить номер\t2 - Изменить номер\t3 - Выход\n'))
            if changes == 1:
                phone_number = input('Номер телефона: ')
                phonebook.setdefault(name_surname, []).append(phone_number)
                for key, value in phonebook.items():
                    print(key, ':', value)
            elif changes == 2:
                phone_number = input('Номер телефона: ')
                phonebook[name_surname] = phone_number
                for key, value in phonebook.items():
                    print(key, ':', value)
            else:
                continue
        else:
            phone_number = (input('Номер телефона: '))
            phonebook.setdefault(name_surname, []).append(phone_number)
            for key, value in phonebook.items():
                print(key, ':', value)
    elif action == 2:
        surname = input('Фамилия: ')
        for key, value in phonebook.items():
            if key[1].startswith(surname[:-2]):
                print(key, value)
    else:
        break
