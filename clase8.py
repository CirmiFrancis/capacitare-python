# Me guié con el código de 'Codeshare'.

# Ejercicio 1
## Pedir al usuario que ingrese su nombre, cantidad de alumnos y cantidad de materias. 
## Luego, pedir e imprimir por cada materia: el nombre de esta y la nota de dicho alumno.

'''
print("=================================================")
nroMaterias = int (input('Ingresa la CANTIDAD de MATERIAS: '))
# nroAlumnos = int (input('Ingresa la CANTIDAD de ALUMNOS: '))
nombreAlumno = input('Ingresa el NOMBRE del ALUMNO: ').strip().capitalize()
arrayFinal = []
for i in range(nroMaterias):
    print("-")
    materia = input(f'Ingresa el NOMBRE de la MATERIA {i+1}: ').strip().capitalize()
    nota = int (input(f'Ingresa la NOTA del ALUMNO {i+1}: '))
    arrayFinal.append((materia,nota)) # uso una tupla en vez de un conjunto {} para que la información esté ordenada
print(f"-----\nEl alumno {nombreAlumno}, obtuvo los siguientes resultados en las siguientes materias: \n{arrayFinal}") #\n es un salto de línea, ahorra líneas de código pero en mi opinión es menos entendible/legible a priori
print("=================================================")
'''

# Ejercicio 2
## Declarar un conjunto de productos (a elección, mínimo 3) con sus precios y stock
## Pedir al usuario que ingrese el producto que quiere comprar y la cantidad
## Verificar si hay stock
## Imprimir a detalle si la compra se pudo realizar o no

'''
productosPreciosStock = [  # Producto, Precio, Stock
    ['Pan',50,100], 
    ['Queso',100,200], 
    ['Carne',150,300] 
]

print("=================================================")
pedidoProducto = input('Ingresa el PRODUCTO que quieres comprar: ').strip().capitalize()
pedidoCantidad = int( input('Ingresa la CANTIDAD que quieres comprar: ') )
pedido = (pedidoProducto,None,pedidoCantidad)

for i in range( len(productosPreciosStock) ): # recorremos el array
    if pedido[0] in productosPreciosStock[i][0]: # buscamos el producto especificado
        print('-\nProducto encontrado')
        if pedido[2] <= productosPreciosStock[i][2]: # preguntamos el stock
            print('-\nHay stock')
            productosPreciosStock[i][2] -= pedido[2] # actualizamos el stock
            print(f'-\nEl pedido realizado fue: {pedido}. La compra fue exitosa.')
            print(f'-\nEl stock de los productos fue actualizado: {productosPreciosStock}') # devolvemos el stock actualizado
            break
        else:
            print('-\nStock insuficiente')
            break
    else:
        if i+1 == len(productosPreciosStock):
            print('-\nProducto NO encontrado')
print("=================================================")
'''

# Ejercicio 3
## Al código anterior
## -Hacer un sistema de 'Carrito de Compras' para permitir al usuario que compre varios productos
## -Usar el precio de cada producto para sumarlos y generar el precio total
## -Si el usuario tiene dinero suficiente, puede realizar la compra, de lo contrario, es rechazada
## -Aplicar un sistema de 'Cupones de Descuentos' (10%, 20% y 50%)

## Los cupones no los agregué porque no hice el sistema teniendo en cuenta eso, así que tendría que cambiar la lógica
## Igual es fácil, más abajo dejé un código basado en uno de un tal "cristian" como ejemplo

'''
print("==================================================================================================")

productosPreciosStock = [  # Producto, Precio, Stock
    ['Pan',50,100], 
    ['Queso',100,200], 
    ['Carne',150,300] 
]
dinero = int( input('Ingresa la CANTIDAD de dinero que tienes: $') ) # pedimos el dinero
carrito = [] # creamos el carrito

yellow = "\033[93m"
reset = "\033[0m"

flag = True # ciclo de varias compras

while flag:
    pedidoProducto = input('-\nIngresa el PRODUCTO que quieres comprar: ').strip().capitalize()
    pedidoCantidad = int( input('Ingresa la CANTIDAD que quieres comprar: ') )
    pedido = (pedidoProducto,pedidoCantidad)

    for i in range( len(productosPreciosStock) ):
        if pedido[0] in productosPreciosStock[i][0]:
            print('-\n*Producto encontrado*')
            if dinero >= productosPreciosStock[i][1]*pedido[1]:
                print('*Hay dinero*')
                if pedido[1] <= productosPreciosStock[i][2]:
                    print('*Hay stock*')
                    productosPreciosStock[i][2] -= pedido[1]
                    dinero -= productosPreciosStock[i][1]*pedido[1]
                    carrito.append(pedido)
                    print(f'-\nLa compra fue exitosa.\n-\nEl pedido realizado fue: {pedido}. El dinero restante es ${dinero}.')
                    print(f'El stock de los productos fue actualizado: {productosPreciosStock}')
                    break
                else:
                    print('*Stock insuficiente*')
                    break
            else:
                print('*Dinero insuficiente*')
                break
        else:
            if i+1 == len(productosPreciosStock):
                print('-\n*Producto NO encontrado*')
    
    pregunta = input(f'-\n{yellow}¿Continuar con la compra? ¿SI o NO?: {reset}').strip().lower()
    if pregunta == 'no':
        print(f'-\nEl carrito es el siguiente: {carrito}')
        print(f'El dinero restante es de: ${dinero}')
        flag = False

print("==================================================================================================")
'''

### Código basado en uno ajeno
print("============================================")

valorTotal=int(input("Ingrese VALOR TOTAL de la compra: $"))

codigo10=0.9
codigo20=0.8
codigo50=0.5

print("-\nEl precio sin descuento es: $",valorTotal)
print("El precio con 10% de descuento es: $",valorTotal*codigo10)
print("El precio con 20% de descuento es: $",valorTotal*codigo20)
print("El precio con 50% de descuento es: $",valorTotal*codigo50)

print("============================================")