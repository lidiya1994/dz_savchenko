#Задача 1

# import randon
# a = tuple[randon.randint(0,100)for i in range(10)]
# b = tuple(a)
# print(b)
# print('max', max(a), 'min', min(a))

#Задача2
import random
#a = tuple([random.randint(0, 5)for_in range(10)])
#b = tuple([random.randint(-5, 0)for_in range(10)])
#c = a+b
#print(c, '\n количество нулей:',c.count(0))

#4Даны 2 кортежа
a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
s_a = sum(a)
s_b = sum(b)
if s_a > s_b:
    print("Сумма больше в кортеже -a")
else:
    print("сумма больше в кортеже -b")

print('min a', min(a), 'Номер -'a.index(a)))
print('min b', min(b), 'Номер -'b.index(b)))
