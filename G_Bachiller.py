#Pedir a, b y c de la formula
print("Este algoritmo esta hecho para resolver la formula ax^2+bx+c")
a= float(input("Ingresar el coeficiente de a: "))
b= float(input("Ingresar el coeficiente de b: "))
c= float(input("Ingresar el coeficiente de c: "))

#Proceso, calcular primero el determinante para saber si existe o no respuesta
det =(b**2)-(4*a*c)

#Evaluar si hay soluciones o no

if det>=0: #Si existen, calcularlas e imprimirlas

    sol1= (-(b)+(det**(1/2)))/(2*a)
    sol2= (-(b)-(det**(1/2)))/(2*a)
    print ("Las soluciones son: ")
    print (f"La solucion 1 es: {sol1}")
    print (f"La solucion 2 es: {sol2}")
    
else:#Sino, imprimir que no es posible encontrar la solucion

    print("La solucion no se encuentra en los reales. <Raiz negativa>")
