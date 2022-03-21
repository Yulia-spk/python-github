# from sys import argv                            #first task
# hours, rate, bonus = map(float, argv[1:])
# print('Заработная плата составит ', hours*rate+bonus)
# print('*'*10)
# a = [int(i) for i in input('Введите исходный список ').split()] #second task
# print([a[i] for i in range(1, len(a)) if a[i] > a[i-1]])
# print('*'*10)
# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])  #third task
# print('*'*10)
# li = [int(i) for i in input('Введите список ').split()]  #fourth task
# print([el for el in li if li.count(el) == 1])
# print('*'*10)
# from functools import reduce    #fifth task
#
#
# def pr(a, b):
#     return a*b
#
#
# li = [el for el in range(100,1001,2)]
# print(reduce(pr, li))
# print('*'*10)
# from sys import argv            #sixth task
# from itertools import count, cycle
# i = 0
# a = 0
# li = []
# for el in count(int(argv[1])):
#     if el > 20:
#         break
#     li.append(el)
# for el in cycle(li):
#     a += 1
#     if a > 50:
#         break
#     print(el)
# print('*'*10)
# def fact(n):     #seventh task
#     if n == 0:
#         print('0!=1')
#     else:
#         for el in (i for i in range(1, n + 1)):
#             yield el
#
#
# a = 1
# for i in fact(int(input('Введите число '))):
#     a = a*i
#     print(f'{i}!={a}')


