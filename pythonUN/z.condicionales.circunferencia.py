'''
DESCRIPCIÓN DEL PROBLEMA
Una persona se detalla que en la pared hay un agujero, y quiere experimentar con un paralelepípedo rectangular para ver si puede 
ingresar por aquel orificio circular. La idea escon las dimensiones del paralelepípedo y de la circunferencia 
decir si pude atravesar la pared con dicho objeto.
ENTRADA
Únicamente cuatro (4) líneas, las cuales las
primeras 3 son las dimensiones, en enteros, 
del paralelepípedo y la última línea es el 
número entero del diametro de la 
circurferencia
SALIDA
Una (1) línea que que diga "Si" si el objeto
puede pasar y "No" si el objeto no puede pasar.
EJEMPLO 
IN	OUT
4	Si
3
10
5
------------------------
4	OUT
3	No
10
4
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

def __esPosible(ancho:int, alto:int, profundo: int, diametro:int):
    if(ancho < diametro and alto < diametro):
        print('Si')
    else:
        print('No')

__esPosible(a,b,c,d)