# Me guié con el código de 'Codeshare'.

# Ejercicio 1
## Pedir al usuario que ingrese un número "límite" y contar e imprimir los números pares e impares.

'''
nroContador = 1
nroIngresado = int( input('Elige un número límite: ') )
listaPar = []
listaImpar = []

while nroContador <= nroIngresado:
    nroDivision = nroContador
    nroDivision %= 2
    if nroDivision == 0:
        listaPar.append(nroContador)
        nroContador += 1
    else:
        listaImpar.append(nroContador)
        nroContador += 1

print('===============================')
print(f'Cantidad de números pares: {len(listaPar)}')
print(listaPar)
print(f'Cantidad de números impares: {len(listaImpar)}')
print(listaImpar)
print('===============================')
'''

# Ejercicio 2
## Pedir al usuario que ingrese una palabra, invertir dicha palabra y comparar ambas para verificar si la palabra es palíndromo.

'''
print('===============================')

palabraIngresada = input('Palabra ingresada: ')
palabraInvertida = ''

for letra in palabraIngresada:
    palabraInvertida = letra + palabraInvertida

print(f'Palabra invertida: {palabraInvertida}')

if palabraIngresada == palabraInvertida:
    print('La palabra ES palíndromo.')
else:
    print('La palabra NO ES palíndromo.')

print('===============================')
'''

# Ejercicio 3
## Pedir al usuario que ingrese una cantidad de exámenes y la nota de cada examen, para calcular el promedio y, en caso de ser mayor a 6, aprobarlo.

print('===============================')

cantidadExamenes = int( input('Ingresar un número de exámenes: ') )
acumuladorNota = 0

for i in range(cantidadExamenes):
    nota = float( input(f'Ingresa la nota {i+1}: ') )
    acumuladorNota += nota

promedio = acumuladorNota/cantidadExamenes

print(f'El promedio es: {round(promedio, 2)}')

if promedio > 6:
    print('-Aprobado-')
else:
    print('-Desaprobado-')

#Operador Ternario:
#resultado = '-Aprobado-' if promedio > 6 else '-Desaprobado-'
#print(resultado)
 
print('===============================')
