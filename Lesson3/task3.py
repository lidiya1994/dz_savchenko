#Задание#1
a=input('имя пользователя ')
b='Привет ' + a
print(b)
print(a*3)


#Задание 1
#Напишите программу, которая запрашивает у пользователя его имя, а затем выводит строку «Привет, …»,
#где вместо многоточия имя пользователя.А вторая строка выведет имя пользователя с повтором 3 раза.

s1 = input("Введите ваше имя")
s2 = "Привет," + s1
s3 = s1*3
print(s1)
print(s2)


#Задание 2
#Вычеслите сумму цифр случайного трехзначного числа

import random

n = random.randint(100,999)

print(n)

s = str(n)
a = int(s[0])
b = int(s[1])
c = int(s[2])

print(a + b + c)

