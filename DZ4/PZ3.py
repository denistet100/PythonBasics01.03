# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

from requests import get, utils
import decimal
from datetime import date


def currency_rates(url, currency):
    currency = currency.upper()
    print(currency)

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_index = content.find(currency)

    if currency_index != -1:
        res_list = []

        prise_cur_fl = float(content[content.find("<Value>", currency_index) + len("<Value>"):
                                     content.find("</Value>", currency_index)].replace(",", "."))

        prise_cur_dc = decimal.Decimal(prise_cur_fl).quantize(decimal.Decimal('.001'))

        cur_data_srt = (content[content.find('<ValCurs Date="', 1) + len('<ValCurs Date="'):
                                content.find('" name=', 1)])
        cur_data_day = cur_data_srt[:2]
        cur_data_month = cur_data_srt[3:5]
        cur_data_year = cur_data_srt[6:]
        cur_data = date.fromisoformat(f"{cur_data_year}-{cur_data_month}-{cur_data_day}")
        res_list.append(cur_data)
        res_list.append(prise_cur_dc)
        return res_list
    else:
        error = 'Error name currency'
        return error


url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_input = input('Введите валюту: ')
print(f"{currency_rates(url_web, currency_input)}")
