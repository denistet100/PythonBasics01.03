# 2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
# урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# ) для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
# /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
# '/downloads/product_2', '304', '0')
# © geekbrains.ru 15
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re

RE_URL1 = re.compile(r'(^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
RE_URL2 = re.compile(r'(\d{1,2}\/\w+\/\d{4}:\d{2}:\d{2}:\d{2} \S\d{4})] .(\w+)')
RE_URL3 = re.compile(r' (\/\w+\/\w+)')
RE_URL4 = re.compile(r'( \d+)')

# r'(^\w{1,4}\.\w{1,3}\.\w{1,3}\.\w{1,3}\.\w{1,3}\.\w{1,3}\.\w{1,3}\.\w{1,3})'

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for raw in f.readlines():
        remote_addr = RE_URL1.findall(raw)[0]
        request_datetime, request_type = RE_URL2.findall(raw)[0]
        requested_resource = RE_URL3.findall(raw)[0]
        response_code, response_size = RE_URL4.findall(raw)
        print(remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
