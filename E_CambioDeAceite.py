#Pedir datos
km = float(input("Ingresar los Km que ha recorrido su vehiculo: "))

#Proceso
cambios = km//5678
cambios = int(cambios)

#Imprimir datos
if cambios<1:
    print("Su carro no ha tenido cambios de aceite")
else:
    print(f"Su carro ha tenido {cambios} cambios de aceite")
