# import copy              #first task
#
#
# class Matrix:
#     def __init__(self, mat):
#         self.mat = mat
#
#     def __str__(self):
#         s = ''
#         for i in range(len(self.mat)):
#             s = s + '\t'.join(map(str, self.mat[i])) + '\n'
#         return s
#
#     def __add__(self, other):
#
#         summa = copy.deepcopy(self.mat)
#         if len(self.mat) != len(other.mat):
#             return None
#         else:
#             for i in range(len(self.mat)):
#                 for j in range(len(self.mat[i])):
#                     summa[i][j] = self.mat[i][j] + other.mat[i][j]
#             return Matrix(summa)
#
#
# a = Matrix([[1, 2, 3], [4, 5, 6]])
# b = Matrix([[7, 8, 9], [10, 11, 12]])
# print(a)
# print(b)
# print(a + b)

# from abc import ABC, abstractmethod             #second task
#
#
# class Clothes(ABC):
#
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return str(self.data)
#
#     @abstractmethod
#     def calc(self):
#         pass
#
#
# class Coat(Clothes):
#
#     def calc(self):
#         return self.data/6.5 + 0.5
#
#
# class Suit(Clothes):
#
#     def calc(self):
#         return 2 * self.data + 0.3
#
# coat_1 = Coat(62)
# print(coat_1.calc())
# suit_1 = Suit(1.7)
# print(suit_1.calc())

# class Cell:           #third task
#     def __init__(self, cell):
#         self.cell = cell
#         self.simbol = '*'
#
#     def __str__(self):
#         return str(f'Количество ячеек - {self.cell}')
#
#     def __sub__(self, other):
#         return Cell(abs(self.cell - other.cell))
#
#     def __mul__(self, other):
#         return Cell(self.cell * other.cell)
#
#     def __truediv__(self, other):
#         return Cell(self.cell // other.cell)
#
#     def __add__(self, other):
#         return Cell(abs(self.cell + other.cell))
#
#     def make_order(self, count):
#         a = self.cell
#         while a > 0:
#             for el in range(1,count+1):
#                 print(self.simbol, end ='')
#                 a -= 1
#                 if a <= 0:
#                     break
#             print('\n', end = '')
#
#
#
# a = Cell(5)
# b = Cell(10)
# c = Cell(3)
# d = Cell(2)
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(c / d)
#
# a.make_order(3)
# b.make_order(3)
#
# 
