'''
DESCRIPCIÓN DEL PROBLEMA
Su primo quiere practicar lo que aprendió, que son las sumas, restas, multiplicación, división y modulo,
para ello le pide a usted que le ayude, usted está muy ocupado con el proyecto de programación,
así que le hace un programa que ingresa 2 números y la operación, y le arroja el resultado.
ENTRADA
Tres (3) líneas, donde 
la primera línea contiene un número entero,
la segunda línea contiene un número entero y 
la tercera línea contiene un carácter donde
    's' es suma,
    'r' es resta,
    'p' es producto,
    'd' es división y
    'm' es modulo.
SALIDA
Una (1) línea, un número entero que contiene la respuesta de la operación.
EJEMPLO
IN	OUT
3	-3
6
r
-------------------------
20	2
6	
m
'''



import string


a = int(input())
b = int(input())
op = input()
def __calc(a:int, b:int, c:string):
    if(op == 's'):
        print(a+b)
    elif(op == 'r'):
        print(a-b)
    elif(op == 'p'):
        print(a*b)
    elif(op == 'd' and a > b and b != 0):
        print(a/b)
    elif(op == 'm' and b != 0):
        print(a%b)

__calc(a,b,op)