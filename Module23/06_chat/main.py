import os

path_to_chat = os.path.abspath('chat.txt')

user_name = input('Введите ваше имя: ').title()
while True:
    try:

        print('\nВыберите действие: ')
        action = int(input('\n1 - просмотреть чат\n2 - написать сообщение\n3 - выйти из чата\n'))
        print()

        if action == 1:
            with open(path_to_chat, 'r', encoding='utf-8') as chat_file:
                for i_line in chat_file:
                    print(i_line)

        elif action == 2:
            with open(path_to_chat, 'a', encoding='utf-8') as chat_file:
                print('\nВаше сообщение: ')
                user_input = input()
                if user_input == '':
                    raise SyntaxError
                else:
                    chat_file.write(user_name + ': ' + str(user_input) + '\n')
        elif action == 3:
            raise InterruptedError

        else:
            raise ValueError


    except ValueError:
        print('\nОшибка ввода, попробуйте снова')

    except SyntaxError:
        print('Вы забыли ввести сообщение!')

    except InterruptedError:
        print('Вы покинули чат.')
        break

    except FileNotFoundError:
        print('В чате пока тишина!')
