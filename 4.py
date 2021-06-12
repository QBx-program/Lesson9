class Car:
    __Car_count = 0

    def __init__(self, speed, color, name):
        self.speed = speed
        self.start_speed = self.speed
        self.color = color
        self.name = name
        self.is_police = False
        self._go = False
        Car.__Car_count += 1

    def _police(self, is_pol):
        return 'Полицейское ' if self.is_police == True else ''

    def go(self):
        if self._go == False:
            print(f'{Car._police(self,self.is_police)}Авто {self.name} цвета {self.color} поехало, скорость {self.speed}')
            self._go = True
        else:
            self.speed += 10
            print(f'{Car._police(self,self.is_police)}Авто {self.name} увеличило скорость до {self.speed}')

    def speed_min(self):
        if self.speed != 0:
            self.speed = self.speed - 10
            print(f'{Car._police(self, self.is_police)}Авто {self.name} снизило скорость до {self.speed}')

    def stop(self):
        if self._go:
            print(f'{Car._police(self,self.is_police)}Авто {self.name} остановилось')
            self.speed = self.start_speed
            self._go = False
        else:
            print(f'{Car._police(self,self.is_police)}Авто {self.name} уже стоит')

    def turn(self, direction):
        direct = {'right': 'вправо', 'left': 'влево'}
        if direction in direct:
            print(f'{Car._police(self,self.is_police)}Авто {self.name} повернуло {direct[direction]}')
        else:
            print(f'{Car._police(self,self.is_police)}Авто {self.name} двигается прямо')

    def show_speed(self, m_speed=False, max_speed=0):
        speed = self.speed if self._go else 0
        print(f'{Car._police(self,self.is_police)}Авто {self.name} двигается со скоростью: {speed}')
        if m_speed == True and self.speed > max_speed:
            print(f'Превышение скорости на {self.speed - max_speed}!' if max_speed < self.speed and self.is_police != True else '')


class TownCar(Car):

    def run(self):
        Car.show_speed(self, m_speed=True, max_speed=60)

class WorkCar(Car):

    def run(self):
        Car.show_speed(self, m_speed=True, max_speed=40)

class PoliceCar(Car):

    def run(self, ispol=True):
        if ispol:
            self.is_police = True
            print('Режим полиции (без ограничений скорости)')
        else:
            self.is_police = False
            print('Режим полиции отключен')

class SportCar(Car):

    def run(self):
        self.speed = 150
        self._go = True
        print('Режим спорта (скорость 150)')

avto1 = Car(50, 'red', 'Ford')
avto2 = Car(40, 'black', 'Lada')
avto3 = Car(60, 'blue', 'Lexus')

avto2.go()
avto2.go()
avto2.turn('left')
avto2.turn('right')
avto2.show_speed()
avto2.stop()
avto2.go()
WorkCar.run(avto2)
TownCar.run(avto2)
avto2.go()
avto2.go()
avto2.go()
avto2.show_speed()
TownCar.run(avto2)
avto2.show_speed()
SportCar.run(avto2)
avto2.show_speed()
TownCar.run(avto2)
PoliceCar.run(avto2)
avto2.go()
TownCar.run(avto2)
WorkCar.run(avto2)
avto2.speed_min()
PoliceCar.run(avto2, False)
TownCar.run(avto2)
