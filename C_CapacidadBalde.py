#Recibir los datos del usuario
r= float(input("Ingresar el radio del balde a llenar: "))
h= float (input("Ingresar altura del balde a llenar: "))

#Proceso
v =((3.1416) * (r**2) * h)

#Mostrar los resultados
print(f"La capacidad del balde es de {v} unidades al cubo")