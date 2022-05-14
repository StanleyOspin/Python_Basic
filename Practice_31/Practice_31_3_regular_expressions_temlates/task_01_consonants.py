import re

text = r'Even if they are djinns, I will get djinns that can outdjinn them.'

result = re.findall(r'\b[aeiouAEIOU]\w*', text)
print('Слова на гласную:', result)
print('=' * 40)
pattern = r'\b[^aeiouAEIOU\s]\w+'
result = re.findall(pattern, text)
print('Слова на любой символ, кроме гласной: ', result)