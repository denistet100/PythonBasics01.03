# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

from sys import argv
from utils import currency_rates, currency_rates_advanced

url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'

if len(argv) > 1:            # Скрипт должен корректно обрабатывать только одну переданную ему валюту.
    currency_input = argv[1]
    print(f"{argv[0]}:   {currency_rates(url_web, currency_input)}")
    print(f"{argv[0]}:   {currency_rates_advanced(url_web, currency_input)}")
else:
    print('Error name currency')
