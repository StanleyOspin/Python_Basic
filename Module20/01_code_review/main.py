def pairs(dictionary):
    id_st = []
    age = []

    for key, value in dictionary.items():
        id_st.append(key)
        age.append(value['age'])

    return zip(id_st, age)


def intersts_surnames(dictionary):
    interests = []
    surnames = ''

    for key, value in dictionary.items():
        interests += value['interests']
        surnames += value['surname']
    return interests, surnames


students = {

    1: {

        'name': 'Bob',

        'surname': 'Vazovski',

        'age': 23,

        'interests': ['biology, swimming']

    },

    2: {

        'name': 'Rob',

        'surname': 'Stepanov',

        'age': 24,

        'interests': ['math', 'computer games', 'running']

    },

    3: {

        'name': 'Alexander',

        'surname': 'Krug',

        'age': 22,

        'interests': ['languages', 'health food']

    }

}

pairs = pairs(students)
print('Список пар «ID студента — возраст»', list(pairs))
interests, surnames = intersts_surnames(students)
print('Список интересов всех студентов', interests)
print('Общая длина всех фамилий студентов', len(surnames))
