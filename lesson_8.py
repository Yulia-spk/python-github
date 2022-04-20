# class Date:             #first task
#     def __init__(self, date):
#         self.d = date
#
#     @classmethod
#     def count(cls, date):
#         return [int(el) for el in date.split('-')]
#
#     @staticmethod
#     def right(day, month, year):
#         if 1 <= day <= 31 and 1 <= month <= 12 and year == 2022:
#             return f'Все верно!'
#         else:
#             return f'Введите корректную дату!'
#
#     def __str__(self):
#         return f'Current date - {self.d}'
#
# a = Date('10-1-22')
# print(a)
# print(Date.count('10-1-22'))
# print(a.right(10, 13, 2022))

# class Zero(Exception):      #second task
#     def __init__(self, txt):
#         self.txt = txt
#
#
# d1, d2 = input(), input()
# try:
#     d1, d2 = int(d1), int(d2)
#     if d2 == 0:
#         raise Zero('Второе число не должно быть 0!')
# except (ValueError, Zero) as err:
#     print(err)
# else:
#     print(d1/d2)


# class Error(Exception):      #third task
#     def __init__(self, txt):
#         self.txt = txt
#
#
# li = []
# while True:
#     try:
#         el = input('Введите число либо введите stop, чтобы прекратить:')
#         if el == 'stop':
#             break
#         if el.isnumeric():
#             print('Введено число ', el)
#             li.append(int(el))
#         else:
#             raise Error('Вы ввели не число!')
#     except Error as err:
#         print(err)
# print(li)


# from datetime import datetime              #task 4,5,6
#
# class Depot:
#     def __init__(self, title):
#         self.title = title
#         self.lists = {}
#         self.give_lists = {}
#
#     def take_to_depot(self, equipment):
# # внесение в словарь название оборудования, серийный номер и время передачи на склад
#         t = datetime.now()
#         self.lists.update({equipment.serial_number:[equipment.title, self,t]})
#         print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number)+', Дата:'
#               + str(t.day)+'.'+str(t.month)+'.'+str(t.year))
#
#
#     def give_to_depot(self, equipment, other):
# # передача оборудование на другой склад или подразделение
#         t = datetime.now()
#         self.give_lists.update({equipment.serial_number: [equipment.title,other, t]})
#         print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
#             equipment.serial_number) + ', Дата:'
#               + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
#         other.take_to_depot(equipment)
#
#
#     def list_equipments(self):
#         print('На склад '+self.title + ' получено оборудование:')
#         print(self.lists)
#         print('Общее количество: ', len(self.lists))
#         print('Со склада '+self.title + ' выдано оборудование:')
#         print(self.give_lists)
#         print('Общее количество: ', len(self.give_lists))
#
#
#
#
# class Office_equipment:
#     def __init__(self, title, serial_number):
#         self.title = title
#         self.serial_number = serial_number
#
#     def __str__(self):
#         return str(self.title)
#
# class Printer(Office_equipment):
#     def __init__(self,title,serial_number, print_velocity):
#         Office_equipment.__init__(self,title, serial_number)
#         self.print_velocity = print_velocity
#
#     def __str__(self):
#         return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)
#
#
# class Scanner(Office_equipment):
#     def __init__(self, title,serial_number,resolution):
#         Office_equipment.__init__(self,title, serial_number)
#         self.resolution = resolution
#
#     def __str__(self):
#         return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)
#
# class Copier(Office_equipment):
#     def __init__(self, title,serial_number, addit):
#         Office_equipment.__init__(self, title, serial_number)
#         self.addit = addit
#
#     def __str__(self):
#         return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)
#
#
#
# store1 = Depot('Main warehouse')
# store2 = Depot('Small warehouse')
# a = Printer('HP',345678,100)
# b = Scanner('Epson',123456,4000)
# c = Copier('Brother',987654, 50)
# d = Printer('HP',245678,200)
#
# print(a)
# print(b)
# print(c)
#
# store1.take_to_depot(a)
# store1.take_to_depot(b)
# store1.take_to_depot(c)
# store1.take_to_depot(d)
#
# store1.give_to_depot(a,store2)
#
# store1.list_equipments()
# store2.list_equipments()


class ComplexNumber:   #seventh task
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно:')
        return f'z = {(self.a * other.a) - (self.b * other.b)} + ({(self.a * other.b) + (self.b * other.a)}* i)'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


comp_1 = ComplexNumber(3, -2)
comp_2 = ComplexNumber(23, 7)
print(comp_2)
print(comp_1 + comp_2)
print(comp_1 * comp_2)