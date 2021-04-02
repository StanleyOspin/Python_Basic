def find_new_card(graphics_card):
    new_model = graphics_card[0]
    for i in range(1, len(graphics_card)):
        if graphics_card[i] > new_model:
            new_model = graphics_card[i]
    return new_model


quantity = int(input('Кол-во видеокарт: '))
graphics_card = []

for i in range(quantity):
    print(i + 1, 'Видеокарта:', end=' ')
    model = int(input())
    graphics_card.append(model)

new_model = find_new_card(graphics_card)
new_list_cards = []

for model in range(len(graphics_card)):
    if graphics_card[model] != new_model:
        new_list_cards.append(graphics_card[model])

print()
print('\nСтарый список видеокарт: ', graphics_card)
print('Новый список видеокарт: ', new_list_cards)
