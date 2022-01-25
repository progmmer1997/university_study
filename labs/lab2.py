
b=["Й","Ц","К","И","Э","Г","Н"]
s=input("Ввведите предложение")
k=0
for i in range(len(s)):
     if s[i] in b:
         k+=1
print(k)