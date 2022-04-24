# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


with open('nginx_logs.txt') as f:
    requested = []
    for line in f:
        remote_addr, line = line.split(' - - ')
        date, line = line.split('] ')

        # Удаление символа [ из строки даты
        date = date.lstrip('[')

        request_type, other_info = line.rsplit(' /')
        # Удаление символа " из строки даты
        request_type = request_type.lstrip('"')
        requested_resource, other_info = other_info.rsplit(' HTTP')

        requested.append((remote_addr, request_type, requested_resource))

print(requested)
