'''
DESCRIPCIÓN DEL PROBLEMA
Un compañero suyo de la universidad ha tenido la idea de hacer un chaza para recaudar fondos y poder estudiar el 
siguiente semestre. Además sabe que el personal de seguridad de la universidad le puede poner muchos problemas, para
ello le pide a usted que haga un programa donde el ponga la hora del día
y sepa se va a ver problemas con los vigilantes. El horario de los vigilantes es de 8 - 12 y de 13- 16
ENTRADA
Unicamente una línea (1) que es un número entero que representa la hora a ingresar de su compañero.
SALIDA
Unicamente una línea (1) con el texto "Si" si tienen problemas al ingresar o un "No" el caso contrario.
EJEMPLO
IN	OUT
11	Si
'''
hora = int(input())

def __verificarHora(hour:int):
    if(hour in range(8,12) or hour in range(13,16)):
        print('Si')
    else: 
        print('No')

__verificarHora(hora)