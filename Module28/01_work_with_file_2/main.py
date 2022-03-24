import os


class File:
    """Kласс File — контекстный менеджер для работы с файлами."""

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'File':
        if not os.path.isfile(self.filename):
            self.mode = 'w'
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file#Все равно ругается, несмотря на то, что в __init__ определил параметр

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        self.file.close()
        return True


with File('test.txt', 'r') as file:
    file.write('Всем привет!')
