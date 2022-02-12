import os
from typing import Iterable


def gen_files_path(link: str, search: str) -> Iterable[str]:
    for link, dirs, files in os.walk(link):
        for file in files:
            if link.endswith(search):
                yield os.path.join(link, file)


path = os.path.abspath(os.path.join('..', '..', '..', 'python_basic'))
directory = '03_files_path'
print()

for file in gen_files_path(path, directory):
    print(file)
