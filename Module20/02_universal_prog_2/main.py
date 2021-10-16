def is_prime(index):
    if index < 2:
        return False
    elif index == 2:
        return True
    divider = 2
    while index % divider != 0:
        divider += 1
    return index == divider


def prime_index(user_input):
    if isinstance(user_input, dict):
        return [user_input[item] for index, item in enumerate(user_input) if is_prime(index)]

    else:
        return [item for index, item in enumerate(user_input) if is_prime(index)]


# user_input = [100, 200, 300, 'буква', 0, 2, 'а', 'b', 'c', 8, 10, 15]
# user_input = (100, 200, 300, 'буква', 0, 2, 'а')
user_input = 'О Дивный Новый мир!'
# user_input = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
result = prime_index(user_input)
print('Результат: ', result)
