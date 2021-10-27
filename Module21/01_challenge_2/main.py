def chelange_2(number):
    if number != 0:
        chelange_2(number - 1)
        print(number)


chelange_2(10)
