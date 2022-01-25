n=int(input())
for i in range(n):
    a = int(input("Xbckj: "))
    th=a//1000
    hundreds=a//100%10
    tens=(a%100)//10
    e=a%10
    if a>0:
        print(th+hundreds,tens+e)
    elif a<0:
        print("Вы введли отрицательное число")
