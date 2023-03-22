#Vocal o Consonante
vocales = "AaEeIiOUu"

#Pedir caracter
r=input("Ingresar caracter a evaluar: ")

#Proceso
any = False
cont=0
while cont<len(vocales):
    if r == vocales[cont]:
        any = True
    cont+=1 
    
#Impresion
if any == False:
    print("Es una consonate")
else:
    print("Es una vocal")
