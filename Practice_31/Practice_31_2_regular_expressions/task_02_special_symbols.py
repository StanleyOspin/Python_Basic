import re

text = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'

result = re.findall(r'\\wwood\+\?\,', text)
print('Список всех упоминаний шаблона:', result)