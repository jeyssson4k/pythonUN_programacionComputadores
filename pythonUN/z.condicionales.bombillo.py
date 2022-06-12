'''
DESCRIPCIÓN DEL PROBLEMA
A un electricista le han encargado el cableado de una luz un tanto especial. El bombillo sirve con ayuda de 3 interruptores, además se sabe
que el bombillo se prende si y solo si al menos hay 2 interruptores encendidos. Usted quiere practicar y genera un programa que se le 
ingresa el estado de cada interruptor e indica si el bombillo esta encendido o apagado
ENTRADA
Tres (3) líneas que indican el estado de los 3 interruptores, siendo 1 prendido y 0 apagado.
SALIDA
Una unica línia que dice "Encendido" o "Apagado" segun sea el caso.
EJEMPLO 
IN	OUT
1	Encendido
0
1
------------------------------------
1	Apagado
0
0
'''



a = int(input())
b = int(input())
c = int(input())
if(a==1):
    if(b==1 or c==1):
        print('Encendido')
    else:
        print('Apagado')
elif(b==1):
    if(c==1):
        print('Encendido')
    else:
        print('Apagado')
else:
    print('Apagado')