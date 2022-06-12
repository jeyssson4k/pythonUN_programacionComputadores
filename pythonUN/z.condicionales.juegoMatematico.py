'''
DESCRIPCIÓN DEL PROBLEMA
Una prima quiere un nuevo juego para poder distraerce pero a su vez practicar el cáculo mental. 
Por ello usted se ingenia un mini juego el cual consiste en poner 2 números, 
si el primero es mayor que el segundo se restan,
si el primero es menor que el segundo se suman,
pero si se igualan los números se deben multiplicar.
ENTRADA
Únicamente dos (2) líneas, los cuales son dos números enteros. 
SALIDA
Únicamente una (1) línea, el cual es resultado correspondiente, es un número entero.
EJEMPLO
IN	OUT
6	3
3
--------------------------
3	9
6
--------------------------
6	36
6
'''
a = int(input())
b = int(input())

def __juegoMatematico(a:int,b:int):
    if(a == b):
        print(a*b)
    elif(a > b):
        print(a-b)
    else:
        print(a+b)

__juegoMatematico(a,b)