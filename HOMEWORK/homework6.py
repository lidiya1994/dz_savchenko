import random
number = random.randint(1,10)
colors = random.randint(1,2)
print(number)
print(colors)
i = 0
while i< 5:
    i += 1
    a = int(input("Введите число: "))
    if a > number:
        print("Ваше число больше заганного")
        print("У вас осталось {5 - i - u} попытки ")
    elif a < number:
        print("Ваше число меньше заганного")
        print(f"у вас осталось {5-i-u} попытки ")
    else:
        print(f"Вы отгадли число с {i+u} попытки")
        break
else:
    while u <=2:
        u += 1
        b = input("Цвет")


print(f"у вас закончились попытки, загаданное число={number}, цвет {colors}")