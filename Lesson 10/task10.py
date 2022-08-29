#Задание 1
lst = [0,0,1,2,3,4,5,6,7]
st = set(lst)
print(len(st) == len(lst))
# #Задание 2
# st = {"jan","feb","march","apr"}
# frozenset.st = frozenset({"jan","feb",-50,30})


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
rezult = int(a)/int(b)
try:
except ZeroDivisionError:
    print("Что-то пошл не так")
else:
    print("Результат в квадрате:",result**2)

finally:
    print("Конец")

