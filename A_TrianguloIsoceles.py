#Pedir los datos al usuario
a= float(input("Ingrese la longitud de los lados iguales: "))
b= float(input("Ingrese la longitud del otro lado: "))

# Operaciones 
perimetro = 2*a + b
altura = (a**2 -(b**2)/4)**(1/2)
area = (b*altura)/2

#Imprimir resultados
print(f"El perimetro es {perimetro}, la altura es {altura} y el area es {area}")
 