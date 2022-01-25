n=int(input("Entering count of the  repetition: "))
for i in range(n):
        number = int(input("Entering number: "))
        number=abs(number)

        hundrends =number // 100
        tens = number // 10 % 10
        ones = number % 10
        print(hundrends,tens,ones)
        if hundrends>0 and tens>=0 and ones>=0:print("Diguits product of your number is: ", hundrends * tens * ones)
        if hundrends==0: print("This number is'n exist")
        elif number<0:

                print("product is",hundrends*tens*ones)


