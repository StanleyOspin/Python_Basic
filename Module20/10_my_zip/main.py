# base_program
def min_length(string, numbers):
    return min(len(string), len(numbers))


string = 'abcd'
numbers = (10, 20, 30, 40)

generator = ((string[i], numbers[i]) for i in range(min_length(string, numbers)))
print(generator)
for i in (generator):
    print(i)


# additional_program

def min_length(data_1, data_2):
    return min(len(data_1), len(data_2))


def function_zip(data_1, data_2):
    if isinstance(data_1, dict):
        generator = ((data_1[i + 1], data_2[i]) for i in range(min_length(data_1, data_2)))

    elif isinstance(data_2, dict):
        generator = ((data_1[i], data_2[i + 1]) for i in range(min_length(data_1, data_2)))

    else:
        generator = ((data_1[i], data_2[i]) for i in range(min_length(data_1, data_2)))
    return generator


string = 'abcd'
numbers_list = [10, 20, 30, 40]
numbers_tuple = (50, 60, 70, 80)
numbers_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

generator = function_zip(numbers_dict, string)
print(generator)
for i in generator:
    print(i)
