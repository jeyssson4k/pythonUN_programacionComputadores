'''
DESCRIPCIÓN DEL PROBLEMA
Pepito esta aprendiendo sobre los tipos de triangulo, y el crea un programa para saber si lo que esta diciendo esta bien o no.
El programa que Pepito hizo, solo es para clasificar segun la longitud de sus lados.
ENTRADA
Tres (3) líneas que indican cada una de las longitudes de los lados de un triangulo
SALIDA
Una unica línia que dice que tipo de trinagulo es "Equilátero", "Isósceles " o "Escaleno".
EJEMPLO
IN	OUT
6	Equilatero
6
6
--------------------------------
6	Isosceles
6
4
--------------------------------
6	Escaleno
5
4
'''
a = int(input())
b = int(input())
c = int(input())

def __clasificaTriangulosPorLados(a:int,b:int,c:int):
    if(a == b and a == c):
        print('Equilatero')
    elif( a != b and a != c and b != c):
        print('Escaleno')
    else:
        print('Isosceles')

__clasificaTriangulosPorLados(a,b,c)