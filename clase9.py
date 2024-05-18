# Clase 9 - Repaso Listas (Arrays)

# ALGUNAS FUNCIONES:

# append(elemento): 
# Agrega un elemento al final de la lista.

# extend(iterable): 
# Extiende la lista agregando elementos desde otro iterable.

# insert(posición, elemento): 
# Inserta un elemento en una posición específica en la lista.

# remove(elemento): 
# Elimina la primera aparición del elemento especificado en la lista.

# pop([índice]): 
# Elimina y devuelve el elemento en la posición especificada, o el último elemento si no se especifica ningún índice.

# index(elemento): 
# Devuelve el índice de la primera aparición del elemento en la lista.

# count(elemento): 
# Devuelve el número de veces que aparece el elemento en la lista.

# sort(): 
# Ordena la lista en orden ascendente.

# reverse(): 
# Invierte el orden de los elementos en la lista.

# ========================================================================

# 'Diccionario' no entra dentro del programa pero lo vimos por arriba. 
# Es iterable y se debe de buscar el valor por su clave.
# La estructura de un diccionario es:
# diccionario = {
#     "clave": "valor",
#     "clave2": "valor2"
# }

#dic = {
#    "nombre": "juan",
#    "edad": 25
#}
#print(dic)

#dic["alumno"] = "si, es alumno"

#print(dic)
#print(dic.keys()) # mostrar claves
#print(dic.values()) # mostrar valores
#print(dic.items()) # mostrar ambas

#del dic["alumno"] # elimina una clave-valor

# ¡¡¡¡¡¡¡¡¡¡ EJERCICIO EXTRA: Adaptar el 'Ejercicio 2' de la clase8.py usando diccionario !!!!!!!!!!
# ¡¡¡¡¡¡¡¡¡¡ EJERCICIO EXTRA: Adaptar el 'Ejercicio 4' de la clase9.py usando diccionario !!!!!!!!!!

#productos = { # diccionarios dentro de un diccionario
#    "tv": {"precio": 80, "stock": 10},
#    "pc": {"precio": 80, "stock": 5}
#}

#print(productos) # imprime el diccionario
#print(productos["tv"]["precio"]) # busca la clave "tv" y dentro de este busca la clave "precio" para imprimir su valor

#producto = productos["tv"] # obtiene la clave-valor correspondiente a "tv", de productos
#print(producto["stock"]) # imprime el valor de la clave "stock" de la variable "producto"

# ======================================================================================================================

# Ejercicio 1: Cuponeras de Descuentos

# Crea un programa que simule una cuponera de descuentos con tres cupones disponibles: “DESCUENTO_10”, “DESCUENTO_20” y “DESCUENTO_50”.
# El programa debe preguntar al usuario el monto total de la compra y luego solicitar el código del cupón. Si el código del cupón es válido, aplicar un descuento al monto total de la compra y mostrar el monto final después del descuento. Si el código del cupón no es válido, mostrar un mensaje indicando que el cupón no es válido y mostrar el monto total sin descuento. 
# Será un plus en este ejercicio crear dos listas para almacenar el precio final de cada venta con y sin descuentos.

'''
print('=============================================================')
montoTotal = int( input('Ingresa el monto total de la compra: $') )
cuponDescuento = input('Ingresa el código del cupón: ')

match cuponDescuento:
    case 'DESCUENTO_10':
        print('-\nAplicando descuento del 10%...')
        montoTotal *= 0.9
    case 'DESCUENTO_20':
        print('-\nAplicando descuento del 20%...')
        montoTotal *= 0.8
    case 'DESCUENTO_50':
        print('-\nAplicando descuento del 50%...')
        montoTotal *= 0.5
    case _:
        print('-\nDescuento inválido.')

print(f'-\nEl monto total a pagar es de: ${montoTotal}')
print('=============================================================')
'''

# Ejercicio 2: Sistema de Facturación

# Crear el código para un e-commerce en el cual los productos tienen un precio y una cantidad en inventario.
# El programa debe tomar como entrada el nombre del producto y también la cantidad que el cliente quiere comprar. 
# Luego se debe verificar si hay suficiente cantidad para satisfacer la solicitud del cliente. 
# -> Si hay suficiente cantidad en el inventario, el programa debe calcular el total a abonar. 
# -> Si no hay suficiente, debe mostrar un mensaje indicando que el producto está agotado.
# Una vez finalizada la venta preguntar si desea realizar una venta más, en caso de no realizar más ventas imprimir el total de facturación diario y la cantidad en inventario que quedó disponible.

'''
print("==================================================================================================")

yellow = "\033[93m"
reset = "\033[0m"

productosPreciosStock = [  # Producto, Precio, Stock
    ['Pan',50,100], 
    ['Queso',100,200], 
    ['Carne',150,300] 
]
#print(f'LISTA DE PRODUCTOS:\n{productosPreciosStock}')
def printAllProducts(): # hice el stock variable por si reutilizaba la función. El nombre y el precio no cambiarían.
    print(f'{yellow}LISTA DE PRODUCTOS:{reset} \
        \nPan   ({productosPreciosStock[0][2]}) - $50  c/u \
        \nQueso ({productosPreciosStock[1][2]}) - $100 c/u \
        \nCarne ({productosPreciosStock[2][2]}) - $150 c/u')
printAllProducts()

#dinero = int( input('-\nIngresa la CANTIDAD de dinero que tienes: $') ) # pedimos el dinero
dineroPorCompra = 0
dineroTotal = 0
carrito = [] # creamos el carrito

flag = True # ciclo de varias compras

while flag:
    pedidoProducto = input('-\nIngresa el PRODUCTO que quieres comprar: ').strip().capitalize()
    pedidoCantidad = int( input('Ingresa la CANTIDAD que quieres comprar: ') )
    pedido = (pedidoProducto,pedidoCantidad)

    for i in range( len(productosPreciosStock) ):
        if pedido[0] in productosPreciosStock[i][0]:
            print('-\n*Producto encontrado*')
#            if dinero >= productosPreciosStock[i][1]*pedido[1]:
#                print('*Hay dinero*')
            if pedido[1] <= productosPreciosStock[i][2]:
                print('*Hay stock*')
                productosPreciosStock[i][2] -= pedido[1]
                dineroPorCompra = productosPreciosStock[i][1]*pedido[1]
                dineroTotal += dineroPorCompra
                carrito.append(pedido)
                print(f'-\nEl pedido realizado fue: {pedido}. El dinero a abonar sería de ${dineroPorCompra}.')
                print(f'El stock de los productos fue actualizado: {productosPreciosStock}')
                break
            else:
                print('*Stock insuficiente*')
                break
#            else:
#                print('*Dinero insuficiente*')
#                break
        else:
            if i+1 == len(productosPreciosStock):
                print('-\n*Producto NO encontrado*')
    
    pregunta = input(f'-\n{yellow}¿Continuar con la compra? ¿SI o NO?: {reset}').strip().lower()
    if pregunta == 'no':
        print(f'-\nEl carrito es el siguiente: {carrito}')
        print(f'El dinero TOTAL a abonar es de: ${dineroTotal}')
        flag = False

print("==================================================================================================")
'''

# Ejercicio 3: Registro de Notas Escolares

# Crea un programa que solicite al usuario ingresar las notas de los estudiantes de una clase.
# El programa debe calcular el promedio de las notas y determinar si cada estudiante aprobó o reprobó. Un estudiante aprueba si su nota es igual o mayor a 6. El programa debe imprimir el nombre del estudiante y si está aprobado o desaprobado.
# Una vez que se terminaron de ingresar los registros de nombres y notas imprimir cantidad de alumnos aprobados y desaprobados, también imprimir cual es el promedio de los aprobados y cual es el promedio general.
# Será un plus en este ejercicio imprimir nombre y nota del alumno con la nota más alta.


print("=================================================")

yellow = "\033[93m"
reset = "\033[0m"

nroAlumnos = int( input('Ingresa la CANTIDAD de ESTUDIANTES: ') )
nroMaterias = int (input('Ingresa la CANTIDAD de MATERIAS: '))

cantidadAprobados = 0
cantidadDesaprobados = 0

sumatoriaPromediosAprobados = 0
sumatoriaPromediosGeneral = 0
promedioAprobados = 0
promedioGeneral = 0

promedioMasAlto = 0
alumnoPromedioMasAlto = ''

for i in range(nroAlumnos):
    nombreAlumno = input(f'-\nIngresa el NOMBRE del ALUMNO {i+1}: ').strip().capitalize()
    arrayNotas = []

    for i in range(nroMaterias):
        nota = float (input(f'Ingresa la NOTA {i+1}: '))
        arrayNotas.append(nota)

    promedioAlumno = sum(arrayNotas) / len(arrayNotas)

    if promedioAlumno >= 6:
        resultadoCursada = 'Aprobado'
        cantidadAprobados += 1
        sumatoriaPromediosAprobados += promedioAlumno
    else:
        resultadoCursada = 'Desaprobado'
        cantidadDesaprobados += 1

    sumatoriaPromediosGeneral += promedioAlumno 

    if promedioAlumno > promedioMasAlto:
        promedioMasAlto = promedioAlumno
        alumnoPromedioMasAlto = nombreAlumno

    print(f'-\n{yellow}El alumno {nombreAlumno} obtuvo las siguientes notas: {arrayNotas} \
        \n* PROMEDIO: {round(promedioAlumno,2)} \
        \n* ESTADO: {resultadoCursada}{reset}')

promedioAprobados = sumatoriaPromediosAprobados / cantidadAprobados
promedioGeneral = sumatoriaPromediosGeneral / (cantidadAprobados + cantidadDesaprobados)

print(f'-\n{yellow}* PROMEDIO de los APROBADOS: {round(promedioAprobados,2)} \
    \n* PROMEDIO GENERAL: {round(promedioGeneral,2)}{reset}')

print(f'-\n{yellow}* ALUMNO con el PROMEDIO MÁS ALTO: {alumnoPromedioMasAlto} \
    \n* PROMEDIO MÁS ALTO: {round(promedioMasAlto,2)}{reset}')

print("=================================================")


# Ejercicio 4: Sistema de Reservas de Cine

# Crear un sistema de reservas para un cine. El cine tiene una lista de 5 películas y X cantidad de asientos disponibles para cada película. 
# El programa deberá permitir a los usuarios elegir una película e ingresar la cantidad de boletos que desean reservar, luego se deberá verificar si hay suficientes asientos disponibles para la reserva. 
# -> Si hay suficientes asientos, debe mostrar un mensaje confirmando la reserva. 
# -> Si no hay suficientes asientos, debe mostrar un mensaje indicando que no hay suficientes asientos disponibles y ofrecer asientos para las películas que sí cuenten con esa cantidad de asientos disponibles.

'''
print("=================================================")

yellow = "\033[93m"
reset = "\033[0m"

# Nombre | Asientos
pelicula1 = ['Tu nombre',50]
pelicula2 = ['Busqueda implacable',80]
pelicula3 = ['Una voz silenciosa',30]
pelicula4 = ['Harry potter y la piedra filosofal',100]
pelicula5 = ['Toy story',120]

cinePeliculas = [pelicula1,pelicula2,pelicula3,pelicula4,pelicula5]
print(f'{yellow}Películas disponibles:\n{cinePeliculas}{reset}')

peliculaEncontrada = False
flag = True

def peliculaConAsientosDisponibles(cantidadBoletos):
    lista = []
    for i in cinePeliculas:
        if i[1] >= cantidadBoletos:
            lista.append(i[0])
    if lista == []:
        print(f'-\n{yellow}No hay ninguna película con esa cantidad de asientos disponibles.{reset}')
    else:
        print(f'-\n{yellow}Te recomendamos estas otras películas que sí tienen esa cantidad de asientos disponibles:\n{lista}{reset}')

while flag:
    peliculaElegida = input('-\nElige una PELÍCULA: ').strip().capitalize()
    cantidadBoletos = int( input('Escribe la CANTIDAD de BOLETOS a reservar: ') )

    for i in cinePeliculas:
        if peliculaElegida == i[0]:
            print('-\n*Película encontrada*')
            peliculaEncontrada = True
            if cantidadBoletos <= i[1]:
                print('*Asientos suficientes*')
                print(f'-\n{yellow}COMPRA REALIZADA: {peliculaElegida}, {cantidadBoletos} boletos.{reset}')
                flag = False
                break
            else:
                print('*Asientos insuficientes*')
                peliculaConAsientosDisponibles(cantidadBoletos)
                break

    if not(peliculaEncontrada):
        print(f'-\n{yellow}*Película NO encontrada*{reset}') 
        flag = False

    if flag:
        respuesta = input('-\n¿Quieres ver otra película? ¿SI o NO? ').strip().lower()
        if respuesta == 'no':
            flag = False
        else:
            flag = True

print("=================================================")
'''

# EJERCICIO EXTRA: Adaptar el 'Ejercicio 2' de la clase8.py usando diccionario
## Declarar un conjunto de productos (a elección, mínimo 3) con sus precios y stock
## Pedir al usuario que ingrese el producto que quiere comprar y la cantidad
## Verificar si hay stock
## Imprimir a detalle si la compra se pudo realizar o no

'''
print("=================================================")

yellow = "\033[93m"
reset = "\033[0m"

productosPreciosStock = {
    "pan": {"precio": 50, "stock": 100},
    "queso": {"precio": 100, "stock": 200},
    "carne": {"precio": 150, "stock": 300},
}

print(f'{yellow}{productosPreciosStock}{reset}')

pedidoProducto = input('Ingresa el PRODUCTO que quieres comprar: ').strip().lower()
pedidoCantidad = int( input('Ingresa la CANTIDAD que quieres comprar: ') )

if pedidoProducto in productosPreciosStock:
    print('-\n*Producto encontrado*')
    if productosPreciosStock[pedidoProducto]["stock"] >= pedidoCantidad:
        print('*Hay stock*')
        productosPreciosStock[pedidoProducto]["stock"] -= pedidoCantidad # actualizamos el stock
        print(f'-\n{yellow}El pedido realizado fue: {pedidoProducto, pedidoCantidad}. La compra fue exitosa.{reset}')
        print(f'{yellow}El stock del producto fue actualizado: {productosPreciosStock[pedidoProducto]}{reset}') # devolvemos el stock actualizado
    else:
        print('*Stock insuficiente*')
else:
    print('-\n*Producto NO encontrado*')
print("=================================================")
'''

# EJERCICIO EXTRA: Adaptar el Ejercicio 4 'Sistema de Reservas de Cine' usando diccionario
## Crear un sistema de reservas para un cine. El cine tiene una lista de 5 películas y X cantidad de asientos disponibles para cada película. 
## El programa deberá permitir a los usuarios elegir una película e ingresar la cantidad de boletos que desean reservar, luego se deberá verificar si hay suficientes asientos disponibles para la reserva. 
## -> Si hay suficientes asientos, debe mostrar un mensaje confirmando la reserva. 
## -> Si no hay suficientes asientos, debe mostrar un mensaje indicando que no hay suficientes asientos disponibles y ofrecer asientos para las películas que sí cuenten con esa cantidad de asientos disponibles.

'''
print("=================================================")

yellow = "\033[93m"
reset = "\033[0m"

cinePeliculas = {
    "tu nombre": 50,
    "busqueda implacable": 80,
    "una voz silenciosa": 30,
    "harry potter y la piedra filosofal": 100,
    "toy story": 120,
}

print(f'{yellow}Películas disponibles:\n{cinePeliculas}{reset}')

flag = True

while flag:
    peliculaElegida = input('-\nElige una PELÍCULA: ').strip().lower()
    cantidadBoletos = int( input('Escribe la CANTIDAD de BOLETOS a reservar: ') )

    if peliculaElegida in cinePeliculas:
        print('-\n*Película encontrada*')
        if cinePeliculas[peliculaElegida] >= cantidadBoletos:
            print('*Asientos suficientes*')
            cinePeliculas[peliculaElegida] -= cantidadBoletos # actualizamos la cantidad de asientos
            print(f'-\n{yellow}El pedido realizado fue: {peliculaElegida, cantidadBoletos}. La compra fue exitosa.{reset}')
            print(f'{yellow}La cantidad de asientos fue actualizada: {cinePeliculas[peliculaElegida]}{reset}') # devolvemos la cantidad de asientos actualizada
            flag = False
        else:
            print('*Asientos insuficientes*')
    else:
        print(f'-\n{yellow}*Película NO encontrada*{reset}') 
        flag = False

    if flag:
        respuesta = input('-\n¿Quieres ver otra película? ¿SI o NO? ').strip().lower()
        if respuesta == 'no':
            flag = False
        else:
            flag = True

print("=================================================")
'''