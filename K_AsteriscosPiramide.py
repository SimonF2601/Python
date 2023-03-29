n = 1 
m = 0 

while n >= m:
    a = int(input("Ingresar numero de asteriscos: "))
    if a % 2 != 0:
        while n <= a:
            while n > m:
                m += 1
                print('*', end='')
            print(' ')
            n += 2
            m = 0
        n -= 4
        while n >= 1:
            while n > m:
                print('*', end='')
                m += 1
            print(' ')
            n -= 2
            m = 0
    else:
        print('Ingrese un numero impar')
