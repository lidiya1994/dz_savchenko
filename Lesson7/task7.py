#1.даны действительные числа х и у. Получить
# |x|-|y|
# 1+|xy|
# x = int(input('Введите число'))
# y = int(input('Введите число'))
# print((abc(x) - abc(y)/abc(x*y))))

#2.Даны катеты прямоугольного треугольника.Найди его гипутенузу и площадь

import math
AB = input("длина первого катета:")
AC = input("длина второго катета:")

#строки переводим в числа

AB = float(AB)
AC = float(AC)

#Находим гипотенузу по теореме пифагора

BC = math. sqrt(AB**2+AC**2)

#Находим площадь
S = (AB*AC)/2


#3.Создать переменные a,b,c и присвоить им значение 9, 17, 5

a = 9
b = 17
c = 5

print(a>b)
print(a!=b+c)
print(b==a+b)
print(c<=a+b)
print(a<b and a<c )    #(c<a<b)
print(b>a or b>c)

#4.Перевести строку в массив по пробелу

s = "I love arrays they are my favorite"
print(s.split(" "))

b = "I love arrays they are my favorite"
b_replace=b.replace('arrays','lists')
b_split = b_replace.split(" ")
print(b_split)

#5 Дан список ["I", "love", "lists", "they", "are", "my", "favorite"]

a = ["I", "love", "lists", "they", "are", "my", "favorite"]
a[2] = 'arrays'
a_join = ''.join(a)
print(a_join)

#6 Даны несколько списков:[-8,1,2,-2,0],[1,-1,0,-9,4,-5],[1,4,0,23,6,34]
a = [-8,1,2,-2,0]
b = [1,-1,0,-9,4,-5]
c =[1,4,0,23,6,34]
a.sort()
b.sort()
c.sort()
print(a[1])
print(b[1])
print(c[1])

#7 Дан список цветов:'red','green','white','black','pink','yellow'.Создайте еще 1 список и переместите в него 1-ый,5 ,6 элементы

a = ["red","green","white","black","pink","yellow"]

b = [a[0],a[4],a[5]]
print(b)

#8.Даны два целых числа m и n. Напишите прорамму, которая выводит все числа от m до n включительно в порядоке возрастания,
#если m<n, или в порядке убывания в противном случае


