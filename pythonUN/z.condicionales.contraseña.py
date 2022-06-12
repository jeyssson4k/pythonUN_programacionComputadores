'''
Descripción del problema
Un joven está probando un sistema de contraseñas, para ello primero pregunta por una clave y después
pregunta por una posible clave, si ambas contraseñas coinciden debe mostrar "Felicidades" y si fallas debe 
aparecer "Error"
Entrada
Se compone de 2 líneas, la primaria línea es una cadena de caracteres y la segunda línea es una cadena de 
caracteres
Salida
Una única línea que es una cadena de caracteres que es un "Felicidades" o un "Error", si la mcontraseña está 
correcta.
Ejemplo
IN        OUT
ABcd  Felicidades
ABcd
'''

import string


password = input()
confirm = input()

def __verificarContraseña(passw:string,confirm:string):
    if(passw == confirm):
        print('Felicidades')
    else:
        print('Error')

__verificarContraseña(password,confirm)