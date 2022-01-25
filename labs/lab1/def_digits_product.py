count = int(input("Entering count: "))
number=int(input("intering number: "))
def digits_product(count:int,n:int):
   for num in range(count):
      n=number
    hundrends = n // 100
    tens = n// 10 %10
    ones=n%10
    if hundrends>0 and tens>=0 and ones>=0:
     print("Diguits product of your number is: ", hundrends * tens * ones)
     if hundrends == 0:
      print("This number is'n exist")
     elif n < 0:
          print("product is", hundrends * tens * ones)
digits_product(count,number)