import os

path = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))

for item in os.listdir(path):
    print()
    print(os.path.abspath(os.path.join('..', '..', '..', item)))
