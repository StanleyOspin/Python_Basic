from typing import Dict, Union

grades: Dict[str, Union[str, int]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
                                      {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37},
                                      {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},

                                      {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2},
                                      {'name': 'Mary', 'score': 63},

                                      {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44},
                                      {'name': 'Richard', 'score': 78},

                                      {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13},
                                      {'name': 'Lloyd', 'score': 52},

                                      {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40},
                                      {'name': 'James', 'score': 54},

                                      {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9},
                                      {'name': 'Bruce', 'score': 68},

                                      {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22},
                                      {'name': 'Aaron', 'score': 3},

                                      {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94},
                                      {'name': 'Sandra', 'score': 40},

                                      ]


def foo_max(grades):
    max_value = 0
    for i in grades:
        for k, v in i.items():
            value = i.get('score')
            if value > max_value:
                max_value = value
    return max_value


print(foo_max(grades))


def foo_min(grades):
    min_value = 100 ** 6
    for i in grades:
        for k, v in i.items():
            value = i.get('score')
            if value < min_value:
                min_value = value
    return min_value


print(foo_min(grades))

maximal_score = max(grades, key=lambda item: item['score'])
print(maximal_score['score'])
minimal_score = min(grades, key=lambda item: item['score'])
print(minimal_score['score'])