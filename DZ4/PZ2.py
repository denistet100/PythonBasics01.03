# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового
# типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

from requests import get, utils
import decimal


def currency_rates(url, currency):
    currency = currency.upper()
    print(currency)

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # print(response)
    # print(encodings)
    # print(content)
    currency_index = content.find(currency)
    # print(currency_index)

    if currency_index != -1:
        # for ch_index in range(content.find("<Value>", currency_index) + len("<Value>"),
        # content.find("</Value>", currency_index), 1):
        # prise_cur = decimal.Decimal(content[content.find( "<Value>", currency_index) + len("<Value>"):
        # content.find("</Value>", currency_index)])
        # Сразу вывели цену валюты в типе для денег, из контекста по индексам от валюты до валюты\

        prise_cur_fl = float(content[content.find("<Value>", currency_index) + len("<Value>"):
                                     content.find("</Value>", currency_index)].replace(",", "."))
        # Я не навижу эту запятую! Часа два не мог понять что не так! А ТАМ ТОЧКА ДОЛЖНА БЫТЬ!!!!

        prise_cur_dc = decimal.Decimal(prise_cur_fl).quantize(decimal.Decimal('.001'))
        return prise_cur_dc
    else:
        error = 'Error name currency'
        return error


url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_input = input('Введите валюту: ')
print(f"{currency_rates(url_web, currency_input)}")
