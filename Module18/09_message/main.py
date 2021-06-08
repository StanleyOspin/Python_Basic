message = input('Сообщение: ').split()
new_message = []

for i in message:
    i = i[::-1]
    if i.startswith((',', '.', '!', '?', ':', ';')):
        i = i[1:] + i[0]
    new_message.append(i)

print(' '.join(new_message))
