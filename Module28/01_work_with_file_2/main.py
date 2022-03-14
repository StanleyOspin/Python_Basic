class File:
    """Kласс File — контекстный менеджер для работы с файлами."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = 'w'

    def __enter__(self) -> 'File':
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        self.file.close()
        return True


with File('test.txt') as file:
    file.write('Всем привет!')
