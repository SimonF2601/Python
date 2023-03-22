""""
Escriba un programa que le pida al usuario una palabra o frase y una letra. El programa deberá imprimir
la misma frase o palabra ingresada, pero ocultando la letra que ingresó el usuario con un asterisco.
 """
#Pedir  datos al usuario
palabra=input("Ingresar palabra o frase a evaluar: ")
letra=input("Caracter o letra a ocultar: ")

#Crear variables auxiliares
new =""
cont= 0

#Proceso
while cont<len(palabra):
    #Evaluacion   
    if palabra[cont]==letra:
        new+="*"
    else:
        new+=palabra[cont]
    cont+=1

#Impresion del resultado
print(new)

