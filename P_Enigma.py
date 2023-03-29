#Crear una cadena con los caracteres del abecedario
abc = "abcdefghijklmnopqrstuvwxyz" #25 posiciones
saltos=27

palabra=input(("Ingresar palabra o frase (En minusculas): "))
while saltos<0 or saltos>=26:
    saltos=int(input("Ingresar numero de saltos por letra (Entre 1 y 25): "))
    
    
cont= 0 #Sirve para llevar la cuenta de la posicion en la que va ir evaluando el programa.
new=" " #Funciona para crear la palabra nueva.

#Proceso a realizar
while cont<(len(palabra)): #Limitar el ciclo hasta el tamaño de la palabra o frase  
    i=0
    while i<26:
        if palabra[cont]==abc[i]:
            if (i+saltos)>25:
                i-=25
                new+=abc[(i-1)+saltos]
            else:
                new+=abc[i+saltos]
            i=26
            
        elif palabra[cont]==" ":
            i=27
            new+=" "
            
        i+=1
    cont+=1

print(new)
                


