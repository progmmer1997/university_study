
n=int(input("Введитекол-во повторений: "))
for i in range(n):
    a, b, c = int(input("Введите первое число: ")), int(input("ведите 2 число: ")), int(input("Введите третье число: "))
    pr = a * b * c
    sr_ar = (a + b + c) // 3
    if a>0 and b>0 and c>0:
        print("Summma",a+b+c,sep=":")
        print("composition",pr,sep=':')
        print("sr-arr",sr_ar,sep=':')
    elif a<0 and b<0 and c<0:
        print("Summma", a+b+c, sep="-")
        print("composition", pr, sep='-')
        print("sr-arr", sr_ar, sep='-')
    elif a==0 and  b==0 and c==0:
        print("Summma", a+b+c, sep=":")
        print("composition", pr, sep=':')
        print("sr-arr", sr_ar, sep=':')
    elif a < 0 or  b< 0 or c < 0:
        print("Summma", a+b+c, sep="=")
        print("composition", pr, sep='=')
        print("sr-arr", sr_ar, sep='=')