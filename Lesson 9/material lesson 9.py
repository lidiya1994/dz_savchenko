#


#В третих, с помощью метода fromkeys:

d = dict.fromkeys(['a','b'])
d_2 = dict.fromkeys(['a','b'],100)
print(d,'\n',d_2)

# в четвертых, с помощью генераторов словарей

d = {a: a**2 for a in range (7)} #синтаксис случайных словарей (а-ключ,а**2-значение)
print(d)

d = {1: 2,2: 4,3: 9}  #
d[4] = 4**2 #[4]элемент имеет имя ключа , после равно может быть любое число, значение

print(d[1]) # (имя ключа)
print(d)


# методы словарей


months = {1:'jan',2:'Feb',3:'Mar',
          4:'Apr',5:'May',6:'Jun',
          7:'Jul',8:'Aug',9:'Sep',
          10:'Oct',11:'Nov',12:'Dec'}
count = len( months)

print(count)


#Работа со словарем

#Обход словаря с помощью цикла for

#Исходный словарь

#Цикл for обхода словаря

#в цикле mn-ключ, Months[mn]-значение

months = {1:'jan',2:'Feb',3:'Mar',
          4:'Apr',5:'May',6:'Jun',
          7:'Jul',8:'Aug',9:'Sep',
          10:'Oct',11:'Nov',12:'Dec'}

for mn in Months:
    print(mn,':',Months[mn])


#Операция del - удаление элемента из словаря

# Исходный словарь

Salary = {'Director':120800.0,'Secretary':101150.25,'Locksmith':188200.00}

print(Salary)

# Удалить элемент по ключу'Secretary'

del Salary['Secretary']

print(Salary)

# Попытка удалить несуществующий ключ
#del Salary[5] -так нельзя, генерируются исключение KeyError:
#del Salary['None']- тоже запрещено

# Position = {'Manager':{'Director',
#                        'Deputy Director'}
#             'Teacher': {'Specialist'
#                         'Methodist':}}
#
# count1 = len(Position)
# count2 = len(Position['Manager'])
# count3 = len(Position['Staff'])
#
# print(Position,'len:', count1,'\n',
#       Position['Manager'],'len:',count2,'\n',
#       Position['Staff'],'len:', count3,'\n',)

#Словари. Функция zip()
#Создание словаря из списков ключей и значений

a = dict(zip([1,2,3],['one','two','three']))
print(a)

#Сортировка словаря

