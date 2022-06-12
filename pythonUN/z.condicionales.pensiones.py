'''
Descripción del problema
El sistema pensional en Colombia se maneja 2 regímenes para las pensiones, régimen de ahorro y régimen de media prima. 
Su principal diferencia es la cantidad de semanas cotizadas, la primera necesita 1150 semanas y la segunda necesita 1300. 
Y las edades se mantienen igual, 57 mujeres y 62 hombres. La registraduría lo contrata a usted para saber si una persona 
cumple los requisitos para poder pensionarse.
Entrada
Se compone de 4 líneas, la primaria línea es un número entro que representa las semanas cotizadas, la 
segunda línea es un carácter que representa el sexo de la persona "M" y "F", la tercera línea es un número 
entero que representa la edad de la persona y la cuarta línea es un valor booleano es un True si está en 
régimen de ahorro y un False en el otro régimen.
Salida
Una única línea que es una cadena de caracteres que es un "Si" o un "No", si puede o no llegar a la pensión.
Ejemplo
IN        OUT
1150   Si
F
57
True
'''
import string


semanas = int(input())
sexo = input()
edad = int(input())
esAhorro = bool(input())

def __esPensionado(cantSemanas:int, sexo:string, edad:int, regimen:bool):
    
    if(sexo == 'F' and edad >= 57):
        if((cantSemanas == 1150 and regimen == True) or (cantSemanas == 1300 and regimen == False)):
            print('Si')
    elif(sexo == 'M' and edad >= 62):
        if((cantSemanas == 1150 and regimen == True) or (cantSemanas == 1300 and regimen == False)):
            print('Si')
    else:
        print('No')


__esPensionado(semanas,sexo,edad,esAhorro)