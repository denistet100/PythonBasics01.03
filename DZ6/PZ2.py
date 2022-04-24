# 2. * (вместо 1)
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt') as f:
    requested = []
    spamer = {}
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
        spamer.setdefault(remote_addr, 0)
        spamer[remote_addr] += 1

print(requested)

spam_dict = sorted(spamer.items(), key=lambda x: x[1], reverse=True)
print(spamer[:5])
