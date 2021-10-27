def function_zip(arg_1, arg_2):
    arg_1 = sorted(list(arg_1))
    arg_2 = sorted(list(arg_2))

    generator = ((arg_1[item], arg_2[item]) for item in range(min(len(arg_1), len(arg_2))))

    return generator


string = 'abcd'
numbers_list = [80, 90, 100, 110]
numbers_tuple = (50, 60, 70, 80, 90)
numbers_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
numbers_set = {10, 20, 30, 40}

# generator = function_zip(numbers_dict, numbers_list)
# generator = function_zip(string, numbers_tuple)
generator = function_zip(numbers_set, numbers_tuple)

for i in generator:
    print(i)
