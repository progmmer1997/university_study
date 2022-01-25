import  math
n=int(input("Введите количество повторений: "))
for i in range(n):

    first_cathet,second_caet=int(input()),int(input() )
    if first_cathet>0 and second_caet>0:
        print("гипотенуза",math.hypot(first_cathet,second_caet))
    elif first_cathet<=0:
        print("такогл катета а нет")
    elif second_caet<=0:
        print("такогл катета b нет")
