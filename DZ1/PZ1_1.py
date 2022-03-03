# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# :)

time = int(input("Введите время в секундах: "))

sek = time % 60
minute = (time - sek) % 3600 // 60
hour = (time - sek - minute) % (3600 * 24) // 3600
day = (time - sek - minute - hour) // (24 * 3600)

result = f'Time is: {day}:{hour:02}:{minute:02}:{sek:02}'
if day == 0 and hour == 0 and minute == 0:
    print(sek, 'сек')
elif day == 0 and hour == 0:
    print(minute, 'мин', sek, 'сек')
elif day == 0:
    print(hour, 'час', minute, 'мин', sek, 'сек')
else:
    print(day, 'дня', hour, 'час', minute, 'мин', sek, 'сек')
