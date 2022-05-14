import re

text = r'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match(r'wo', text)
print('Поиск шаблона в начале строки:', result)
print('=' * 40)
result = re.search(r'wo', text)
print('Поиск первого найденного совпадения по шаблону:', result)
print('Содержимое найденной подстроки:', result.group(0))
print('Начальная позиция:', result.start())
print('Конечная позиция:', result.end())
print('=' * 40)
result = re.findall(r'wo', text)
print('Список всех упоминаний шаблона:', result)
print('=' * 40)
result = re.sub(r'wo', r'ЗАМЕНА', text)
print('Текст после замены:', result)