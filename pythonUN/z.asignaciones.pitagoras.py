'''
Descripción del problema 
Juanito está aprendiendo sobre el teorema de Pitágoras, para repasar lo aprendido le pide a usted que diseñe un programa 
que ingresé 2 catetos y muestre la hipotenusa.
Entrada
2 líneas dónde son números reales
Salida 
1 línea que es un número reales 
Ejemplo 
IN       OUT
4.0      5.0
3.0
'''
from math import sqrt


a = float(input())
b = float(input())

def __calcularHipotenusa(catetoA:float,catetoB:float):
    return(
        sqrt(a**2 + b**2)
    )

c = __calcularHipotenusa(a,b)
print(c)