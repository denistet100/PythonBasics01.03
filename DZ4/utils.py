from requests import get, utils
import decimal
from datetime import date


def currency_rates(url, currency):
    currency = currency.upper()
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)  # Информация с сайта
    currency_index = content.find(currency)  # нашли индекс названия валюты в контексте, если не существует = -1

    if currency_index != -1:
        prise_cur_fl = float(content[content.find("<Value>", currency_index) + len("<Value>"):
                                     content.find("</Value>", currency_index)].replace(",", "."))
        prise_cur_dc = decimal.Decimal(prise_cur_fl).quantize(decimal.Decimal('.001'))
        return prise_cur_dc
    else:
        error = 'Error name currency'
        return error


def currency_rates_advanced(url, currency):
    currency = currency.upper()

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)  # Информация с сайта
    currency_index = content.find(currency)  # нашли индекс названия валюты в контексте, если не существует = -1

    if currency_index != -1:
        res_list = []
        prise_cur_fl = float(content[content.find("<Value>", currency_index) + len("<Value>"):
                                     content.find("</Value>", currency_index)].replace(",", "."))
        prise_cur_dc = decimal.Decimal(prise_cur_fl).quantize(decimal.Decimal('.001'))
        cur_data_srt = (content[content.find('<ValCurs Date="', 1) + len('<ValCurs Date="'):
                                content.find('" name=', 1)])
        cur_data_day = cur_data_srt[0:2]
        cur_data_month = cur_data_srt[3:5]
        cur_data_year = cur_data_srt[6:]
        cur_data = date.fromisoformat(f"{cur_data_year}-{cur_data_month}-{cur_data_day}")
        res_list.append(cur_data)
        res_list.append(prise_cur_dc)
        return res_list
    else:
        error = 'Error name currency'
        return error


if __name__ == '__main__':
    url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'
    # Тест
    print('url_web = "http://www.cbr.ru/scripts/XML_daily.asp"', '\n',
          currency_rates(url_web, "USd"), '\n',
          currency_rates(url_web, "EuR"), '\n',
          currency_rates(url_web, "GBP"), '\n',
          currency_rates(url_web, "GBP2"), '\n')

    # Тест
    print('url_web = "http://www.cbr.ru/scripts/XML_daily.asp"', '\n',
          currency_rates_advanced(url_web, "USd"), '\n',
          currency_rates_advanced(url_web, "EuR"), '\n',
          currency_rates_advanced(url_web, "GBP"), '\n',
          currency_rates_advanced(url_web, "GBP2"), '\n')
