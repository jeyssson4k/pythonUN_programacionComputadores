'''
Descripción del problema
Para el problema de las contraseñas una parte importante es averiguar si es en mayúscula o en minúscula un 
carácter del alfabeto, para ello diseñe un programa que haga la división.
Entrada
Una única línea el cual es un carácter.
Salida
Una única línea que es un "min" o un "may" dependiendo el caso 
Ejemplo
IN    OUT
A     may(65,90)(97,122)
'''
import string


a = input()

def __upperOrLower(char:string):
    if(ord(char) in range(65,90)):
        print('may')
    elif(ord(char) in range(97,122)):
        print('min')
    else:
        pass

__upperOrLower(a)