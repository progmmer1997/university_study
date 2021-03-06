# аргументы по умолчанию
print("Hello {}, your balance is {}.".format("Adam", 230.2346))
# позиционные аргументы
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))
# аргументы ключевые слова
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))
# смешанные аргументы
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
# целочисленные аргументы
print("The number is:{:d}".format(123))
# аргументы с плавающей точкой
print("The float number is:{:f}".format(123.4567898))
# восьмеричный, двоичный и шестнадцатеричный формат
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
# целые числа с минимальной шириной
print("{:5d}".format(12))

# ширина не работает для чисел длиннее заполнения
print("{:2d}".format(1234))
# заполнение для чисел с плавающей точкой
print("{:8.3f}".format(12.2346))
# целые числа с минимальной шириной, заполненные нулями
print("{:05d}".format(12))
# заполнение для чисел с плавающей запятой, заполненных нулями
print("{:08.3f}".format(12.2346))
# показать знак +
print("{:+f} {:+f}".format(12.23, -12.23))
# показать знак -
print("{:-f} {:-f}".format(12.23, -12.23))
# показать место для знака +
print("{: f} {: f}".format(12.23, -12.23))
#целые числа с выравниванием по правому краю
print("{:5d}".format(12))
# числа с плавающей точкой с выравниванием по центру
print("{:^10.3f}".format(12.2346))
# выравнивание целого числа по левому краю заполнено нулями
print("{:<05d}".format(12))
# числа с плавающей точкой с выравниванием по центру
print("{:=8.3f}".format(-12.2346))
# отступ строки с выравниванием по левому краю
print("{:5}".format("cat"))
# отступ строки с выравниванием по правому краю
print("{:>5}".format("cat"))
# заполнение строк с выравниванием по центру
print("{:^5}".format("cat"))
# заполнение строк с выравниванием по центру
# и '*' - символ заполнения
print("{:*^5}".format("cat"))
# определяем класс Person
class Person:
    age = 23
    name = "Adam"
# форматирование возраста
print("{p.name}'s age is: {p.age}".format(p=Person()))
# объявляем словарь person
person = {'age': 23, 'name': 'Adam'}
# форматирование возраста
print("{p[name]}'s age is: {p[age]}".format(p=person))
# объявляем словарь person
person = {'age': 23, 'name': 'Adam'}
# форматирование возраста
print("{name}'s age is: {age}".format(**person))