def div():   #first task
   a = float(input('Введите число '))
   b = float(input('Введите число '))
   if b == 0:
        print('На ноль делить нельзя!')
   else:
       return a/b
print(div())
print('*'*10)
def user(name, surname, year, city, email, phone):     #second task
    ''' Собирает данные о пользователе'''
    print(f'Вас зовут {name} {surname}, вы родились в {year} году, проживаете в {city}, ваш адрес эл.почты - {email},номер вашего телефона - {phone}')
user(name = input('Введите ваше имя '), surname = input('Введите фамилию '), year = int(input('Введите год рождения ')), city = input('Введите город проживания '), email = input('Ваш email '), phone = int(input('Введите номер телефона ')))
print('*'*10)
def my_func():    #third task
    a, b, c = float(input()), float(input()), float(input())
    d = min(a,b,c)
    return a+b+c-d


print(my_func())
print('*'*10)
def my_func(x, y):      #fourth task
    r = x ** y
    print(r)


my_func(float(input('Введите первое число ')), float(input('Введите отрицательное число ')))
print('*'*10)
def my_func():      #fifth task
    a = 0
    s = 0
    while True:
        li = [i for i in input().split()]
        for el in li:
            if el == 's':
                return(print(s))
            else:
                el = float(el)
                s += el
        print(s)


my_func()
print('*'*10)
def int_funct():                          #sixth task
    a = input('Введите слово ')
    if a.islower() and a.isalpha() is True:
        print(a.title())
    else:
        print('Введите только буквы и только маленькие!')
int_funct()
print('*'*10)
def int_funct(a):    #seventh task
    l = 0
    for el in a:
        if 97 <= ord(el) <= 122:
            l += 1
            if l == len(a):
                return a.title()
        else:
            print('Введите только маленькие латинские буквы!')
            return 1


a = [el for el in input('Введите строку ').split()]
li = []
i = 0
for el in a:
    p = int_funct(el)
    if p == 1:
        i += 1
        break
    else:
         li.append(p)
if i == 0:
    print(li)




