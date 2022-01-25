import math
a=int(input("Введите первое число:"))
b=int(input("Ведите второе число:"))
if a>b:
      sq_r=math.pow(a,2)-2*a*b-math.pow(b,2)
      print("Kвадрат разности",sq_r,sep=":")
elif a<b:
        print("Разность квадратов чисел равна",a**2-b**2,sep=",")
elif a==b:
         print("Происходит магия",a**2+b**3,sep="_")
print(type(a),type(b),sep=";")