# Clase 10 - Funciones Generales & Repaso

# isnumeric(): es una función que permite saber si una cadena es numérica.
# isalnum(): es una función que permite saber si una cadena es alfanumérica.
# isalpha(): es una función que permite saber si una cadena es alfanumérica.

palabra = input('Ingresar un dato: ')

while not palabra.isnumeric():
    print('No son números')
    palabra = input('Ingrese nuevamente: ')

palabra = int(palabra)

print('Número ingresado * 2: ', palabra*2)

# juego de piedra-papel-tijera

# import random
# .choice()
# .randrange(0,3) /// .randrange(10)