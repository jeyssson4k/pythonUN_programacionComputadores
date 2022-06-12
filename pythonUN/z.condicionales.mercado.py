'''
DESCRIPCIÓN DEL PROBLEMA
Una tienda de frutas quiere insentivar la venta de sus productos, para ello aplica unos descuentos de la siguiente forma, si se compran 
hasta 3 productos no hay descuento, si se compran de 4 hasta 7 productos se aplica el 5% si se compran de 8 hasta 12 productos se aplica
el 10%, para más de 13 productos se aplica el 15%.
ENTRADA
Dos (2) líneas, donde la primera línea contiene el número entero de productos comprados, y la segunda línea condiene un número real con el 
valor unitario del producto
SALIDA
Una (1) línea, un número real que contiene el valor total a pagar por el cliente
EJEMPLO
IN	OUT
3	3000
1000
'''

a = int(input())
b = int(input())

def __aplicaDescuento(cantidad:int, precio:int):
    if(cantidad <= 3 and cantidad >= 1):
        return precio*1*cantidad
    elif(cantidad >= 4 and cantidad <= 7):
        return precio*0.95*cantidad
    elif(cantidad >= 8 and cantidad <= 12):
        return precio*0.9*cantidad
    else:
        return precio*0.85*cantidad

print(__aplicaDescuento(a,b))