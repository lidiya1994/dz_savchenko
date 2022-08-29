# f = open('example.txt','r')


#print(*f) # выводим содержимое файла
#print(f) #выводим обьект
from typing import TextIO

# f = open('example.txt', 'r')
# try:
#     print(*f)#альтернативный тип закрытия файла
# finally:
#     f.close()
#
# with open('example.txt') as f:
#    print(*f) #работа с файлами
#
# f = open('exemple.txt','r')
#
# print(f.read(7))  #чтение 7 символов из example.txt
# print(f.read(-7))

#
# f = open('xyz.txt', 'w') #открытие в режиме записи
# f.write('Hello\nWorld') #запись Hello World в файл
# f.close()# закрытие файла
#
#
# f = open('xyz.txt','w')
# f.write('Hello\nWorld')
# f.close()
# f = open('xyz.txt','r')
# print(f.read())

            #Переименование файлов в Python
#import os
#os.rename("xyz.txt","abc.txt") #переименование xyz.txt в abc.txt

# import os
# print("текущая деректория:",os.getcwd()) #вывести текущую директорию
#
# os.mkdir("folder")

# import os
#
# os.chdir("folder") #изменение текущего каталога на 'folder'
#
# #вывод текущей папки
# print("Текущая директория изменилась на folder:",os.getcwd())

# import os
# os.chdir("folder") #изменение текущего каталога на 'folder'
#
# os.chdir("..") #вернуться в предыдущую директорию
#
# os.makedirs("nested1/nested2/nested3") # сделайте несколько вложенных папок

# import os
#
# #удалить этот файл
#
# os.remove("abc.txt")

# import os
#
# #удалить папку
#
# os.rmdir("folder")

# import os
#  # удалить вложенные папки
#
# os.removedirs("nested1/nested2/nested3")# Это удалит только пустые каталоги
#


