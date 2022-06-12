'''
DESCRIPCIÓN DEL PROBLEMA
Un compañero suyo de la universidad tiene un emprendimiento con un bar. El compañero se ha dado cuenta que en muchas ocaciones las 
filas para ingresar a su establecimiento son muy largas y la gente se termina llendo a otro lugar. Para evitar esto y hacer el tramite
más rápido le pide diseñar un programa que pregunte la edad y diga si entra o no entra.
ENTRADA
Una unica línea que contenga un entero y este represente la edad de la persona a ingresar
SALIDA
Una unica línea que diga "Puede pasar" si cumple con los requisitos o escriba "No pasa" si no los cumple.
EJEMPLO 
IN	OUT
18	Puede pasar
---------------------------------
15	No pasa
'''

edad = int(input())

def __ingresoBar(e:int):
    if(edad >= 18):
        print('Puede pasar')
    else:
        print('No pasa')
    
__ingresoBar(edad)