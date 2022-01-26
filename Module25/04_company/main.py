from person import Manager, Agent, Worker
from random import randint, choice

names = ['Иван', 'Алексей', 'Александр', 'Петр', 'Василий', 'Владимир', 'Сергей', 'Андрей', 'Дмитрий']
surnames = ['Иванов', 'Петров', 'Сидоров', 'Сергеев', 'Андреев', 'Васильев', 'Дмитриев', 'Алексеев', 'Александров']


def persons():
    name = choice(names)
    surname = choice(surnames)
    age = randint(20, 50)
    return name, surname, age


employees = []

for _ in range(3):
    employees.append(Manager(*persons()))

for _ in range(3):
    agent = Agent(*persons())
    agent.sales = randint(200000, 300000)
    employees.append(agent)


for _ in range(3):
    worker = Worker(*persons())
    worker.working_hours = randint(160, 176)
    employees.append(worker)


for emp in employees:
    print(emp)
