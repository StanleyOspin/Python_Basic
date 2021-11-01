def find_key_in_dictionary(dictionary, key, depth):
    if key in dictionary:
        return dictionary[key]
    if depth > 1:

        for value in dictionary.values():
            if isinstance(value, dict):
                found_key = find_key_in_dictionary(value, key, depth - 1)
                if found_key:
                    break
        else:
            found_key = None

        return found_key


site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}

required_key = input('Какой ключ ищем? ').lower()
user_depth = int(input('Введите глубину поиска: '))
found_key = find_key_in_dictionary(site, required_key, user_depth)

if found_key:
    print(found_key)
else:
    print('Такого ключа в словаре нет.')
