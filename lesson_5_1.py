# l = []                             #first task
# try:
#     with open('test.txt', 'w') as data:
#         while True:
#             a = input("Введите строку ")
#             if a == '' or a.isspace():
#                 break
#             else:
#                 l.append(a+'\n')
#         data.writelines(l)
# except IOError:
#     print('Произошла ошибка ввода-вывода!')

# i = 0       #second task
# with open('test_2.txt', 'r', encoding='utf-8') as data:
#     l = data.readlines()
#     print('Количество строк - ', len(l))
#     data.seek(0)
#     for line in data:
#         i += 1
#         words = [i for i in line.split()]
#         count_words = len(words)
#         print(f'В {i} строке количество слов - {count_words} ')
#
# salary_sum = 0            #third task
# emp = 0
# try:
#     with open('salary.txt', 'r', encoding='utf-8') as data:
#         for line in data:
#             el = [i for i in line.split()]
#             salary_sum += float(el[1])
#             emp += 1
#             if float(el[1]) < 20000:
#                 print(el[0])
#     average_salary = salary_sum/emp
#     print(average_salary)
# except IOError:
#     print(('Ошибка ввода-вывода!'))
#
# new_file = []      # fourth task
# dict = {'One':'Один', 'Two':'Два', 'Three':"Три", 'Four':'Четыре'}
# numbers_1 = open('numbers_1.txt', 'w')
# with open('numbers.txt', 'r', encoding='utf-8') as number:
#     for line in number:
#         line = line.split(' ', 1)
#         new_file.append(dict[line[0]] + ' ' + line[1])
# with open('numbers_1.txt', 'w', encoding='utf-8') as number_1:
#     number_1.writelines(new_file)
#
# from functools import reduce        #fifth task
# with open('task_5.txt', 'w+') as numbers:
#     numbers.write('1 73 45 17 8')
#     numbers.seek(0)
#     a = [int(i) for i in numbers.read().split()]
#     print(a)
#     print(reduce(lambda a, b: a + b, a))
#
# with open('task_6.txt', 'r', encoding='utf-8') as data:   #sixth task
#     for line in data:
#         l = len(line)
#         li = []
#         i = 0
#         while i < l:
#             st = ''
#             s = line[i]
#             while '0' <= s <= '9':
#                 st += s
#                 i += 1
#                 if i < l:
#                     s = line[i]
#                 else:
#                     break
#             i += 1
#             if st != '':
#                 li.append(int(st))
#         summa = lambda a, b: a+b
#         lin = line.split()
#         print(f'{lin[0]} - {sum(li)} часов')

# import json           #seventh task
# with open('task_7_1.json', 'w', encoding='utf-8') as f_write:
#     with open('task_7.txt', 'r', encoding='utf-8') as f_read:
#         profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_read}
#         result = [profit, {'average_profit': sum([int(i) for i in profit.values() if int(i)>0]) /len([int(i) for i in profit.values() if int(i)>0])}]
#
#     json.dump(result, f_write)