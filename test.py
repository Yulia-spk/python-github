age, name = int(input('Ваш возраст: ')), str(input('Ваше имя: '))#first task
b = age+8
print(name, ', в 2030 году Вам будет', b, '!')
print('*'*10)

sec = int(input('Введите время в секундах: '))#second task
hh = sec//3600
mm = (sec//60)-(hh*60)
ss = sec%60
print(f'{hh}:{mm}:{ss}')
print('*'*10)

a = str(input('Введите число: '))#third task
b = int(a+a)
c = int(a+a+a)
a = int(a)
print('Сумма равна:', a+b+c)
print('*'*10)

i = int(input('Введите число: '))#fourth task
b = 0
while i > 0:
    a = i % 10
    if a > b:
        b = a
    i = i//10
print(b)
print('*'*10)

gross, costs = int(input('Введите выручку: ')), int(input('Введите издержки: '))#fifth and sixth task
if gross > costs:
    print('Предприятие отработало с прибылью!')
    n = int(input('Введите количество сотрудников: '))
    rent = (gross-costs)/gross*100
    b = gross/n
    print(f'Рентабельность составляет {rent} процентов, прибыль фирмы в расчете на одного сотрудника равна {b} ')
elif gross == costs:
    print('Прибыль равно нулю.')
else:
    print('Предприятие отработало с убытками.')
print('*'*10)

a, b = int(input('Введите результат первого дня: ')), int(input('Введите расстояние: '))
i = 1
while b >= a:
    a = a+a*0.1
    i += 1
print('На', i, 'день пробежит не менее', b, 'км')





