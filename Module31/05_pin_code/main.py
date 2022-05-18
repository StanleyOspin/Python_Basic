import itertools

if __name__ == '__main__':
    pin = (1, 9, 7, 6)
    digits = range(10)
    pin_code = itertools.product(digits, repeat=4)
    for code in pin_code:
        if code == pin:
            print('Lock is open')
