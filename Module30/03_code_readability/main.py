from typing import List

if __name__ == '__main__':
    is_prime_1: List[int] = list(
        filter(lambda x: all(map(lambda divider: x % divider != 0, range(2, int(x ** 0.5) + 1))), range(2, 1001)))
    print(is_prime_1)
    print()
    is_prime_2: List[int] = [number for number in range(2, 1001) if
                             all(number % divider != 0 for divider in range(2, int(number ** 0.5) + 1))]
    print(list(is_prime_2))
    # TODO надо было также написать вариант на циклах for и сравнить легкость чтения и понимания кода
