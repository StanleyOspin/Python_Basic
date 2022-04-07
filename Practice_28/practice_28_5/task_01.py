from typing import Any


class File:
    """Kласс File — контекстный менеджер для работы с файлами."""

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        self.file.close()


with File('example.txt', 'w') as file:
    file.write('Всем привет!')