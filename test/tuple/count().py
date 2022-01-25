n0,n1,n3,n4,n5='Finn', 'Jake', 'Marceline', 'Princess',' Bubblegum'
names = (n0,n1,'BiMo',n3,n4,n5,'BiMo')

if  names.count(n0)==names.index(n0):
    print(names[0], "is a magic string")
elif names.count(n1)==names.index(n1):
    print(names[1],"is a magic string")
if names.count('BiMo')==names.index('BiMo'):
    print('BiMo','is a magic string')
elif names.count(n3)==names.index(n3):
    print(names[3], "is a magic string")
elif names.count(n4)==names.index(n4):
    print(names[4], "is a magic string")
elif names.count(n5)==names.index(n5):
    print(names[5], "is a magic string")