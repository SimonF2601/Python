#Pedir numero al usuario
n=2
while n%2==0:
    n=int(input("Ingresar un numero impar:"))
    
#Impresion de patron
espacios = 0
while n>0:
    for i in range(1,n+1):
        print("+",end="")
    for j in range(1,espacios+1):
        print(" ", end="")
    for k in range(1, n+1):
        print("+",end="")
    print()
    n-= 2
    espacios+= 4