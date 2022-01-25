n=int(input("Поличество повторений: "))
for i in range(n):
    a=int(input("Введите число: "))
    hundrends=a//100
    tens=a%10//10
    ones=a%10
    print(hundrends,tens,ones)
