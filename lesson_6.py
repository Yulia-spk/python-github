# from time import sleep                #first task
# class TrafficLight:
#     _color = ['красный', 'желтый', 'зеленый']
#     def running (self):
#         i = 0
#         while i < 3:
#             print(f'Цвет светофора: {TrafficLight._color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             else:
#                 sleep(4)
#             i += 1
#
#
# light = TrafficLight()
# light.running()

# class Road:            #second task
#     _lenght = None
#     _width = None
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#
#     def weight(self):
#         per_1 = 25
#         thickness = 5
#         print(f'Необходимое количество асмфальта - {self.lenght * self.width * per_1 * thickness} тонн')
#
#
# road_1 = Road(int(input('Введите длинну дороги: ')), int(input('Введите ширину дороги:')))
# road_1.weight()
# class Worker:                    #third task
#
#     def __init__(self, name, surname, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self._income = {'wage': wage, 'bonus': bonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f'Full name: {self.name} {self.surname}')
#
#
#     def get_total_income(self):
#         total_income = self._income['wage'] + self._income['bonus']
#         print(f'Total income: {total_income}')
#
#
# manager = Position('Ivan', 'Ivanov', 400, 300)
# manager.get_full_name()
# manager.get_total_income()

# class Cars:                #fourth task
#     name = None
#     speed = None
#     color = None
#     is_police = False
#
#     def __init__(self, name, speed, color, is_police=False):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.is_police = is_police
#
#     def info(self):
#         print(f'')
#
#     def go(self):
#         print(f'The car {self.name}  is traveling at a speed of {self.speed} kilometers per hour.')
#
#     def stop(self):
#         print(f'The car {self.name} has stopped')
#
#     def turn(self, direction):
#         print(f'The car {self.name} turned to ' + direction)
#
#     def show_speed(self):
#         print(f'Current speed {self.name} is {self.speed}')
#
#
# class TownCar(Cars):
#
#     def show_speed(self):
#         print(f'Current speed of town car {self.name} is {self.speed}')
#
#         if self.speed > 40:
#             print(f'Speed of {self.name} is higher than allow for town car')
#         else:
#             print(f'Speed of {self.name} is normal for town car')
#
#
# class SportCar(Cars):
#
#     def __int__(self, name, speed, color, is_police, max_speed):
#         super().__init__(self, name, speed, color, is_police)
#         self.max_speed = max_speed
#         print(f'Max speed - {self.max_speed}')
#
#
# class WorkCar(Cars):
#     def show_speed(self):
#         print(f'Current speed of work car {self.name} is {self.speed}')
#
#         if self.speed > 60:
#             print(f'Speed of {self.name} is higher than allowed for work car')
#
# class PoliceCar(Cars):
#
#     def police(self):
#         if self.is_police is True:
#             print(f'{self.name} is from police department')
#         else:
#             print(f'{self.name} is not from police department')
#
# mazda = TownCar('Mazda', 60, 'black')
# mazda.go()
# workcar_1 = WorkCar('VW', 100, 'black', False)
# workcar_1.show_speed()
# police_1 = PoliceCar('Audi', 100, 'red', False)
# police_1.police()

# class Stationery:      #fifth task
#     title = None
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pencil(Stationery):
#     def draw(self):
#         print('Используется карандаш')
#
# class Pen(Stationery):
#     def draw(self):
#         print('Используется ручка')
#
# class Handle(Stationery):
#     def draw(self):
#         print('Используется маркер')
#
# pencil = Pencil()
# pencil.draw()
# pen = Pen()
# pen.draw()
# handle = Handle()
# handle.draw()
