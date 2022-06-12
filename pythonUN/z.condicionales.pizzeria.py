'''
Descripción del problema
Una pizzería de su barrio quiere automatizar el proceso de realizar los pedidos. Primero debe escoger el 
tamaño, pequeño, mediano y grande, después si tiene o no queso, el tipo de carne, pollo, res, cerdo o ninguno,
y por último los vegetales o fruta, piña, tomate, anchoa, espinaca. Solo se puede elegir un ingrediente. Y al final 
debe llegar al pizzero para realizar el pedido.
Entrada
Se compone de 4 líneas, todas las entradas son enteros
Salida
Una única línea que es una cadena de caracteres con todas las métricas de la pizza.

Consejo: Haga un menú 
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

def __infoPizza(size:int,cheese:int,meat:int,vegetables:int):
    tamano = {
        0 : "pequeño",
        1 : "mediano",
        2 : "grande"
    }
    queso = {
        0 : "No",
        1 : "Si"
    }
    carnes = {
        0 : "ninguno",
        1 : "pollo",
        2 : "res",
        3 : "cerdo"
    }
    frutas = {
        0 : "piña",
        1 : "tomate",
        2 : "anchoa",
        3 : "espinaca"
    }
    print(f"Tamaño: {tamano.get(size)}, Lleva queso: {queso.get(cheese)}, Carnes: {carnes.get(meat)}, Vegetales: {frutas.get(vegetables)}")


__infoPizza(a,b,c,d)