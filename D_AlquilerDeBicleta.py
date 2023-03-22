cargo =0
#Pedir datos al usuario
min = int(input("Ingresar en minutos el timepo que alquilo la bicicleta: "))
fm = min

#Proceso
if (min>=100):
    cargo= 7*100
    if (min>1440):
        cargo= cargo + (57*1340) +96000
    else:
        min= min - 100
        cargo = cargo + (57*min)
else:
    cargo = 7*min

#Imprimir cargo
print(f"Su tiempor fue de {fm} minutos. Y su cobro es de {cargo}")