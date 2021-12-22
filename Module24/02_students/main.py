from student import Student


def user_input():
    surname = input('Фамилия: ')
    name = input('Имя: ')
    num_of_group = input('Номер группы: ')
    marks = list(map(int, input('Oценки через пробел: ').split()))
    return surname, name, num_of_group, marks


students = [Student(*user_input()) for _ in range(2)]
students.sort(key=lambda x: x.rating())

for student in students:
    print()
    print(student)
