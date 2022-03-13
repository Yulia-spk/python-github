s = [1, 'dog', 10.2, 'собака']
for i in s:
    type(i)
print('*'*10)
li = [i for i in input('Введите список: ').split()]
for i in range(0, len(li)-1, 2):
    li[i], li[i+1] = li[i+1], li[i]
print(li)
print('*'*10)
s = [i for i in input('Введите строку: ').split()]
for i, el in enumerate(s):
    if len(el) > 10:
        print(i+1, el[:10])
    else:
        print(i+1, el)
print('*'*10)
seazon = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
a = int(input('Введите номер месяца: '))
for key in seazon.keys():
    if a in seazon[key]:
        print(key)
print('*'*10)
s = [10, 2, 34, 34, 56, 7]
s.sort()
s.reverse()
i = 0
p = int(input('Введите число: '))
for i in range(len(s)):
    if p == s[i]:
        if s.count(s[i]) >= 1:
            s.insert(s.index(s[i]) + s.count(s[i]), s[i])
        break
    else:
        if p > s[1]:
            s.insert(0, p)
            break
        if p < s[-1]:
            s.append(p)
            break
    if p < s[i] and p > s[i + 1]:
        s.insert(i + 1, p)
        break
print(s)
print('*'*10)








