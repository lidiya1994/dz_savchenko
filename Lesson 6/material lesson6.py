elements = [1, 3, 'a', 6, 'b']
print(elements)

elements = list()
print(elements)
# Генератор списков
import random

#Объявим список с и заполним его 10 элементами от 0 до 100
c = [random.randint(0,100) for i in range (10)]
print(c[0])
print(c[-1])
print(c[5])
print(c[-4])

# Добавление в список
elements = []

elements.append('a')
elements.append(1)

print(elements)

#Добавление в список на указанную позицию
elements = [1,3,'a',6,'b']
elements.insert(1,2)  #(до зяпятой)позиция по индексу, (после запятой)добавляемый элемент )
print(elements)

# Изменение элементов списка
elements = [1, 3, 'a', 6,'b']
elements[1] = 2 #Замена элемента списка, после равно элемент который хотим поставить вместо индекса заменяют
print(elements)

#Удаление элемента из списка
elements = [1, 3, 'a', 6,'b']
del elements[1] #удаляет по индексу
print(elements)

elements = [1, 3, 'a', 6,'b' ]
elements.remove('a') #удаляет по имени
print(elements)

# Как проверить ниличие элемента в списке

elements = [1, 3, 6, 'a', 'b', 'abc', 123, 435]
if 'abc' in elements:
  print('yes.')

  #Объединение (слияние списков)
a = [1, 3, 5]
b = [1,5,8,9]
print(a+b)

d = ['h','e','l','l','o']
e = ['w','o','r','l','d']

d.extend(e)  #extend не возвращает новый список, а дополняет текущий
print(d)
d.extend('abababab')
print(d)
d.extend('123456789')
print(d)

 #Копирование списка в Python
a = [1,2,3,4]   # это не правильный список копирования
b = a # Переменной b присваивается не значение списка a ,а его адрес

a.append(5)
b.append(6)
print('a',a,'b',b)# Выводим: Первая а коментарий, вторая а список

a = ['кот', 'слон', 'змея']
b = a.copy()
b.append('тигр')
print(a,b)

# Цикл по списку
elements = [1, 2, 3, "meow"]
for i in elements:
 print(i)
elements = [1, 2, 3, "meow"]
elements_len = len(elements)
i = 0
while i < elements_len:
 print(elements[i])
 i += 1

# clear удаляет все элементы
a = [1, 2, 3]
a.clear()
print(a)

# copy
a = [1, 2, 3]
b = a.copy()
print(id(a), id(b),a ,b)

#count
elements = ["one", "two", "three"]


#pop
elements = [1, "meow", 3, "meow"]







#Вложенные списки
a = [1, 2, 3,[ 5, 6, 7],'abc', 3]
a = [["яблоки", 50], ["апельсины",190],["груши",100]]
print(a[0])

print(a[1][0])
