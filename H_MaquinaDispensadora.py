#Pedir el valor a devolver
valor=float(input("Ingresar valor a devolver en monedas: "))
n=valor
x1000=0 
x500=0 
x200=0
x100=0
x50=0

#Proceso
if n>=1000:
    x1000=int(n//1000)
    n-=(x1000*1000)
if n>=500:
    x500=int(n//500)
    n-=(x500*500)
if n>=200:
    x200=int(n//200)
    n-=(x200*200)
if n>=100:
    x100= int(n//100)
    n-=(x100*200)
if n>=50:
    x50 = int(n//50)
    n-=(x50*50)

#Imprimir devuelta
print("Su devuelta de $",int(valor),", se dio de la sigueinte manera (Usando monedas):")
print(f"$ 1000: {x1000}")
print(f"$ 500: {x500}")
print(f"$ 200: {x200}")
print(f"$ 100: {x100}")
print(f"$ 50: {x50}")

#Definir el restante del cambio
if n==0:
    print("Su cambio es exacto")
else:
    print("Su resto es de $",int(n))
