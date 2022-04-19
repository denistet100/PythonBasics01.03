# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ...
# raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

import re

RE_NAME = re.compile(r'(?P<username>^[a-zA-Z0-9]+)\@{1}(?P<domain>[a-z]+\.{1}[a-z]+)$')

email = 'someone@geekbrains.ru'
email0 = 'someo34ne@geekbrains.ru'
email1 = 'someone@geekbrainsru'
email2 = 'someo.ne@geekbrains.ru'
email3 = 'someonegeekbrains.ru'
email4 = 'someone@gee/kbrains.ru'
email5 = 'someone@geekbr.ains.ru'
email6 = 'someone@geek brains.ru'


def email_parse(email_address):
    if RE_NAME.match(email_address) is None:
        raise ValueError
    else:
        print(*map(lambda x: x.groupdict(), RE_NAME.finditer(email_address)), sep=', ')


email_parse(email1)
