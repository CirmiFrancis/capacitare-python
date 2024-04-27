# Me guié con el código de 'Codeshare'.

# Ejercicio 1
## Pedir al usuario que ingrese 3 nùmeros, luego imprimir cùal de ellos es el mayor

'''
nro1 = int( input('Ingrese el primer número: ') )
nro2 = int( input('Ingrese el segundo número: ') )
nro3 = int( input('Ingrese el tercer número: ') )

if nro1 > nro2:
    if nro1 > nro3:
        print(f'El mayor es {nro1}, seguido de {nro2} o {nro3}') 
    else:
            print(f'El mayor es {nro3}, seguido de {nro1} y luego {nro2}') 
elif nro2 > nro3:
    print(f'El mayor es {nro2}, seguido de {nro3} o {nro1}') 
else:
    print(f'El mayor es {nro3}, seguido de {nro2} y luego {nro1}') 
'''

# Ejercicio 2
## Si el monto de una compra es igual o supera los $10000 con 5 productos o más en el carrito, obtiene un descuento del 30%.
## Si el monto de una compra es menor a $10000 con menos de 5 productos en el carrito, obtiene un descuento del 20%.

class colors:
    YELLOW  = '\033[93m'
    RESET   = '\033[0m'

print('==============================================')
precioTotal = float ( input('Ingrese el PRECIO TOTAL de la compra: $ ') )
cantidadProductos = int ( input('Ingrese la CANTIDAD de PRODUCTOS del carrito: ') )

if precioTotal >= 10000 and cantidadProductos >= 5:
    print('-')
    print(f'Precio Original: $ {precioTotal}')
    print(colors.YELLOW + 'Aplicando DESCUENTO del 30%...' + colors.RESET)
    print(f'Precio Final: $ {precioTotal-precioTotal*0.3}')
    print('==============================================')
elif precioTotal < 10000 and cantidadProductos < 5:
    print('-')
    print(f'Precio Original: ${precioTotal}')
    print(colors.YELLOW + 'Aplicando DESCUENTO del 20%...' + colors.RESET)
    print(f'Precio Final: ${precioTotal-precioTotal*0.2}')
    print('==============================================')
else:
    print('-')
    print(colors.YELLOW + 'DESCUENTO NO DISPONIBLE...' + colors.RESET)
    print(f'Precio Final: ${precioTotal}')
    print('==============================================')