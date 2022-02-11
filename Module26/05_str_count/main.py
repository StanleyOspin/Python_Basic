import os
from collections.abc import Iterable


def gen_rows(link: str) -> Iterable[int]:
    for link, dirs, files in os.walk(link):
        for file in files:
            path = os.path.join(link, file)
            if path.endswith('py'):
                with open(path, 'r', encoding='utf-8') as file:
                    row_count = 0
                    for line in file.read().split('\n'):
                        if (not line.strip() == '') and (not line.strip().startswith("#")) and (
                                not line.strip().startswith('"')):
                            row_count += 1
                            yield row_count


link = os.path.abspath(os.path.join('..', '..', 'Module26'))
print(link)
total_count = 0
for i in gen_rows(link):
    total_count += i
print('Total rows quantity:', total_count)
