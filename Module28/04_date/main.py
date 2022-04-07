class Date:
    """Класс Date - проверяет числа даты на корректность\
конвертирует строку даты в объект класса Date, состоящий\
из соответствующих числовых значений дня, месяца и года"""

    def __init__(self, *args) -> None:
        self.day, self.month, self.year = args

    def __str__(self) -> str:
        return 'День: {} \tМесяц: {} \tГод: {}'.format(self.day, self.month, self.year)

    @classmethod
    def parse_date_string(cls, date_str: str) -> map:
        return map(int, date_str.split('-'))

    @classmethod
    def from_string(cls, date_str: str) -> object:
        assert cls.is_date_valid(date_str), 'date is wrong'
        return cls(*cls.parse_date_string(date_str))

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        day, month, year = cls.parse_date_string(date_str)
        return 0 < day <= 31 and 0 < month <= 12 and year > 0


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))

print(Date.is_date_valid('40-12-2077'))

