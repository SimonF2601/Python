# Algoritmo I_CobroStreaming
inicio = input("Ingrese la hora en la que inicio el Streaming de la siguiente manera HH-MM-SS (230512): ")
finalizar = input("Ingrese la hora en la que finalizo el Streaming de la siguiente manera HH-MM-SS (120115): ")

size = len(inicio)
if (size == 5):
    horas = inicio[0]
    minutos = inicio[1:3]
    seg = inicio[3:5]
else:
    horas = inicio[0:2]
    minutos = inicio[2:4]
    seg = inicio[4:6]

size1 = len(finalizar)
if (size1 == 5):
    horas1 = finalizar[0]
    minutos1 = finalizar[1:3]
    seg1 = finalizar[3:5]
else:
    horas1 = finalizar[0:2]
    minutos1 = finalizar[2:4]
    seg1 = finalizar[4:6]

h = int(horas)
m = int(minutos)
s = int(seg)
h1 = int(horas1)
m1 = int(minutos1)
s1 = int(seg1)

if h == h1:
    horaf = 24
    horaf = horaf*3600
else:
    if h > h1:
        h = -1*(h-24)+h1
        horaf = h*3600
    else:
        h = h*3600
        h1 = h1*3600
        horaf = h1-h

segf = s1-s
m = m*60
m1 = m1*60
minutosf = m1-m
segf = segf+minutosf+horaf
cobro = segf*2

if cobro > 1000:
    print("Su cobro es de $", cobro)
else:
    cobro = 1000
    print("Su cobro es de $", cobro)
