#задача1 квадраты всех целых чисел от 1 до 10.
i = 1
while i <= 10:
   print(i**2)
   i += 1

#задача 3 Вычеслите числа от 1 до 15 в порядке убывании.
i = 15
while i >= 0:   #i!=0
   print(i)
   i -= 1

#задание 4
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
while a<b:
   a += 1
   if a == 0:
       break
   print(a)
    #Пример условия else в цикле for
for i in range(3):
   if i == 10:# Введи 2
       break
   print(i)
else:
   print('Готово')
    #Пример условия else в цикле While:
i = 0
while i<3:
   print(i)
   i+=1
else:
   print('Готово')

#Задача5
i=0
a=[]
while i<98:
    i+=7
    a.append(i) #список точка append
print(a, 'Длинна: ', len(a))

#Задача 6
Print("Ноль в качестве знака операции завершит работу программы")
x= float(input("x="))
y= float(input("y="))
while True:
    s = input("Знак(+,-,*,/):")
    if s == '0':
        break
    elif s =='+':
        print(x+y)
    elif s =='-':
        print(x-y)
    elif s =='*':
        print(x*y)
    elif s == '/':
        if y != 0:
            print(x/y)
        else:
            print("Деление на ноль!")

