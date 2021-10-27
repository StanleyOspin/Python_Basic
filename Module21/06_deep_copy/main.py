site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def deep_copy(struct, tag, replace_obj):
    if tag in struct:
        struct[tag] = replace_obj
        return struct

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            deep_copy(sub_struct, tag, replace_obj)


frame_site = {}

site_quantity = int(input('Сколько сайтов: '))

for _ in range(site_quantity):

    client_site = site.copy()  # TODO эта фукнция не обеспечивает копирования вложенных структур данных - используйте
                               #  функцию deepcopy из модуля copy

    name_product = input('Введите название продукта для нового сайта: ')
    h2 = 'У нас самая низкая цена на {0}'.format(name_product)
    title = 'Куплю/продам {0} недорого'.format(name_product)
    deep_copy(client_site, 'title', title)
    deep_copy(client_site, 'h2', h2)
    frame_site[name_product] = client_site
    for key, value in frame_site.items():
        print('Сайт для ', key, ':', sep='')
        print('site =', value)
print(site)  # TODO как видите глобальная переменная изменилась, а этого допустить нельзя
