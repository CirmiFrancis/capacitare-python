# Ejercicio 1
# Pedir al usuario una palabra y contar la cantidad de vocales. Imprimir la cantidad de cada vocal.

'''
palabra = input('Pasame una palabra: ').strip().lower()

# vocales = ['a','e','i','o','u']

contadorVocales = 0
contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0

# flag = True
# print(palabra[0])

for letra in palabra:
    if letra == 'a':
        contadorVocales += 1
        contadorA += 1
    elif letra == 'e':
        contadorVocales += 1
        contadorE += 1
    elif letra == 'i':
        contadorVocales += 1
        contadorI += 1
    elif letra == 'o':
        contadorVocales += 1
        contadorO += 1
    elif letra == 'u':
        contadorVocales += 1
        contadorU += 1

    # if letra in vocales:
    #   contadorVocales
    #   print()

print('========================')
print('Palabra:', palabra)
print('Vocales:', contadorVocales)
print('A:', contadorA)
print('E:', contadorE)
print('I:', contadorI)
print('O:', contadorO)
print('U:', contadorU)
print('========================')
'''

# Ejercicio 2
# Pedir un número al usuario y determinar que es un número primo.

'''
numero = int( input('Pasame un número: ') )
puntero = 1
cantidadDeNumerosConRestoCero = 0

while puntero <= numero:
    if (numero%puntero) == 0:
        cantidadDeNumerosConRestoCero += 1
    puntero += 1
    # resultado = (cantidadDeNumerosConRestoCero + 1) if ((numero%puntero) == 0) else cantidadDeNumerosConRestoCero

print('================================')
if cantidadDeNumerosConRestoCero > 2:
    print(numero, 'no es un número primo.', 'Es divisible por', cantidadDeNumerosConRestoCero, 'números.')
else:
    print(numero, 'es un número primo.', 'Es divisible por', cantidadDeNumerosConRestoCero, 'números.')
print('================================')
'''

# Ejercicio 3
# Escribir un programa que simule una carrera de autos, el programa debe solicitar al usuario ingresar los tiempos de vuelta de cada piloto hasta que ingrese un tiempo negativo que indica el final de la carrera.
# Determinar quien fue el piloto más rápido, el más lento y el tiempo promedio de vuelta de carrera.

'''
nroDePiloto = 1
tiempoTotal = 0
vueltaMasRapida = float('inf') # crea un infinito positivo, para no inicializar en 0 ya que sería el tiempo más bajo
vueltaMasLenta = float('-inf') # crea un infinito negativo
pilotoMasRapido = 0
pilotoMasLento = 0

print('')
while True:
    tiempoDeVuelta = float( input('Ingresa el tiempo de vuelta del piloto: ') )

    if tiempoDeVuelta < 0:
        break

    print(f'El piloto {nroDePiloto} tuvo un tiempo de {tiempoDeVuelta} segundos.')
    tiempoTotal += tiempoDeVuelta

    if tiempoDeVuelta < vueltaMasRapida:
        vueltaMasRapida = tiempoDeVuelta
        pilotoMasRapido = nroDePiloto

    if tiempoDeVuelta > vueltaMasLenta:
        vueltaMasLenta = tiempoDeVuelta
        pilotoMasLento = nroDePiloto
    
    nroDePiloto += 1
    print('')

tiempoPromedio = tiempoTotal/nroDePiloto

print('======================================================================')
print(f'El PILOTO MÁS RÁPIDO fue el número {pilotoMasRapido}, con un TIEMPO de {vueltaMasRapida} segundos.')
print(f'El PILOTO MÁS LENTO fue el número {pilotoMasLento}, con un TIEMPO de {vueltaMasLenta} segundos.')
print(f'El TIEMPO PROMEDIO DE VUELTA es de {round(tiempoPromedio, 3)} segundos.')
print('======================================================================')
'''

# Ejercicio 4
# Desarrollar un programa que permita la gestión de la información de los empleados de una empresa.
# Debe tener las siguientes funcionalidades:
# - Ingresar empleados (nombre, salrio y horas trabajadas)
# - Calcular salario semanal considerando un salario base por hora ($100) y adicional por horas extras ($50) si son más de 40 horas semanales
# - Imprimir en pantalla el nombre salrio semanal y bono de cada empleado

yellow = "\033[93m"
reset = "\033[0m"

flag = True

while flag:
    print('===========================================================================')
    cantidadEmpleados = int( input(f'Ingresa el número de empleados: ') )
    print('===========================================================================')

    arrayEmpleados = []

    for i in range(cantidadEmpleados):
        empleadoNombre = input(f'* NOMBRE del empleado {i+1}: ').strip().lower().capitalize()
        empleadoSalario = int( input(f'* SALARIO de {empleadoNombre}: $') )
        empleadoHoras = int( input(f'* HORAS TRABAJADAS de {empleadoNombre}: ') )

        salarioIngresado = empleadoSalario
        horasExtras = max(empleadoHoras - 40, 0)

        salarioBase = 100 * empleadoHoras
        salarioBono = 50 * horasExtras

        if empleadoHoras > 40:
            empleadoSalario += salarioBase + salarioBono
        else:
            empleadoSalario += salarioBase

        arrayEmpleados.append({empleadoNombre, '$' + str(empleadoSalario)})

        print('')
        print(f'Empleado:          {yellow}{empleadoNombre}{reset}')
        print('')
        print(f'Salario Ingresado: {yellow}${salarioIngresado}{reset}')
        print(f'Salario Base:      {yellow}${salarioBase}{reset}')
        print(f'Salario Bono:      {yellow}${salarioBono}{reset}')
        print('----------------------------')
        print(f'Salario Total:     {yellow}${empleadoSalario}{reset}')
        print('===========================================================================')

    print(arrayEmpleados)
    print('')

    respuesta = input('¿Quieres ingresar más empleados? ¿SI o NO?: ').lower()
    if respuesta == 'no':
        print('===========================================================================')
        flag = False