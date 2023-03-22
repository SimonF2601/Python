#Pedir numero a evaluar
num = int(input("Ingresar numero a evaluar: "))

#Proceso
desicion = num%2

#Imprimir desicion
if desicion == 0:
    print("El numero",num,"es par")
else:
    print("El numero",num, "es impar")