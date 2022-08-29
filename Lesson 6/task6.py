#Задание №1
a = [1, 2, 3]
a.reverse()
print(a)
#Задание №2
list1 = [5,10,15,20,25,50,20]
print("список:\n", list1)

ind = list1.index(20)
list1[ind] = 200
print("Изменненый список: \n", list1)


a = int(input('Введите отрицальное число'))
b = int(input('Введите положительное число'))
while a < b:
    a += 1
    if a == 0:
        break
    print(a)
