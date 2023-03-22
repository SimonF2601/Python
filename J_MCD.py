#Pedir numeros a calcular 
print("Ingresar par de numeros a calcular MCD")
a=int(input("Ingresar primer numero: "))
b=int(input("Ingresar segundo numero: "))

#Decir cual es el mayor y cual es el menor
if a>b:
    Nmayor=a
    Nmenor=b
else:
    Nmayor=b
    Nmenor=a

#Inicializar MCD y contador a usar
MCD=1
cont=2

while cont<=Nmayor and cont<=Nmayor:
    My = Nmayor % cont
    Mn = Nmenor % cont
    if (My==0) and (Mn==0):
        MCD=cont
    cont= cont + 1        
    
#Impirmir resultado
print(f"El MCD de {a} y {b} es {MCD}")