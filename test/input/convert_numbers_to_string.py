print("Добро пожаловать.\n  "
      " Данна программа иллюстрирует преобразование чисел в строкуи  "
      "работу с полученной строкой ")
#преобразование input to int()
int_number=int(input("Введите  целое трехзначное число"))
# преобразование int в str()
s_number=str(int_number)
# Преобразование input to float()
f_number=float(input("Введите трехзначное число с плвающей точкой"))
# преобразование float в str()
f_string=str(f_number)
#print(int_number,f_number,s_number,f_string,sep="\n")
# произведём сложенение численных  переменных (int_number и f_number )
# для чего преобразуем int_number во float()
print("Cумма переменных,содержащих числа  переменных равна: ",round(f_number+float(int_number),3),"\n"
      " Сумма строковых переменных равна",s_number+f_string)
# Произведем умножение сначала численных переменных,а затем строковых:
print("Произведение переменных,содержащих числа  равна ", round(float(2*int_number)+3*f_number,3),
     "\n", "Произведение  строковых переменных равно", s_number+f_string)
# Выводим число в обратном порядлу
#print(int_number)
hundreds=int_number//100
tens=int_number//10%10
units=int_number%10
print( " Hundreds",hundreds,"tens",tens,"units",units)
print("Целое число в обратном порядке",units,tens,hundreds,"\n",
      "Строка в обратном порядке",s_number[2],s_number[1],s_number[0])
