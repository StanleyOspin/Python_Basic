class File:
    """Kласс File — контекстный менеджер для работы с файлами."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = 'w'  # TODO режим открытия файла надо тоже получать через параметр

    def __enter__(self) -> 'File':
        # TODO Тут надо проверить наличие файла c помощью os.path.isfile и если файла нет, то режим открытия поменять
        #  на режим "для записи", то есть 'w'
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file  # TODO РyCharm "ругается" потому, то считается хорошей практикой все используемые атрибуты
                          #  экземпляра класса объявлять в __init__

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        self.file.close()
        return True


with File('test.txt') as file:
    file.write('Всем привет!')
