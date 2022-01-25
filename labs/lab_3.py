
import random

arr = []
print("Исходный список: ")
for i in range(10):
    x = random.randint(0, 100)
    arr.append(x)
    print("%4d" % x, end='')

print()
minim = int(input('Укажите Min: '))
maxim = int(input('Укажите Max: '))
new = [ ]
n=-1
for i in arr:
    n+=1
    if minim <= i <= maxim:
        new.append (n)
if len(new) > 0:
    print ("Всего элементов: ", len(new))
    print ("Список индексов: ", new)
else:
    print ("Нет элементов в диапазоне ")

