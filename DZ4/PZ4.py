# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
# в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

from utils import currency_rates, currency_rates_advanced       # , currency_rates_advanced

url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_input = input('Введите валюту: ')
print(f"{currency_rates(url_web, currency_input)}")
print(f"{currency_rates_advanced(url_web, currency_input)}")
