#Перемножить все нечетные значения в диапазоне от 1 до 100.
pr = 1

for i in range(1,100):
    if i % 2 != 0:
        pr *=i
print(pr)

#Записать в массив все числа в диапазон от 1 до 500 кратные 5

mas = []
for i in range(1,500):
    if i % 5 == 0:
        mas.append(i)
print(mas)

#Вывести на экран все четные значения в диапазоне от 1 до 497
for i in range(1,497):
    if i % 2 == 0:
        print(i, end = " ")


#Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив
mas1 = [1,3,5,3,1]
mas2 = []
for i in mas1:
    if mas1.count(i) >= 2:
       mas2.append(i)
print(mas2)

