# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} go'

    def stop(self):
        return f'{self.name} stop'

    def turn(self, direction):
        return f'{self.name} turns {direction}'

    def show_speed(self):
        return f'{self.name} speed {self.speed}'

class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass


town_car = TownCar(80, 'Red', 'Mazda', False)
sport_car = SportCar(300, 'Blue', 'Porsche', False)
work_car = WorkCar(70, 'Yellow', 'Lada', False)
police_car = PoliceCar(180, 'White-Blue', 'Toyota', True)

print(town_car.show_speed())
print(sport_car.show_speed())
print(work_car.show_speed())
print(police_car.show_speed())
print(sport_car.turn('right'))
print(work_car.turn('left'))
