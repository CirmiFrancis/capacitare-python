# Asumí los temas que pudieron haber visto en esta clase.

# ======================================== ========================================

# Para correr el codigo: 'python3 clase2.py'

# ======================================== OPERADORES ========================================

# -ARITMÉTICOS:    +, -, *, /, //, %, **
# -DE COMPARACIÓN: ==, !=, <, >, <=, >= 
# -LÓGICOS:        and, or, not
# -DE ASIGNACIÓN:  =, +=, -=, *=, /=, //=, %=, **=
# -DE IDENTIDAD:   is, is not
# -DE PERTENENCIA: in, not in

'''
print(100 + 50)
print(100 - 50)
print(100 * 2)
print(100 / 2)
print(100 // 3)
print(100 % 3)
print(2 ** 5)

# ----------------------------------

print('A' == 'a')
print('A' != 'a')
print(1 > 2)
print(1 < 2)
print(1 >= 1)
print(1 <= 1)

# ----------------------------------

print('A' != 'a' and 1 < 2)
print('A' != 'a' or 1 > 2)
print(not('A' != 'a' or 1 > 2))

# ----------------------------------

numero = 10
print(numero)

numero += 2
print(numero)

numero -= 2
print(numero)

numero *= 4
print(numero)

numero /= 2
print(numero)

numero //= 3
print(numero)

numero %= 4
print(numero)

numero **= 5
print(numero)

# ----------------------------------

a = [1, 2, 3]
b = a

print(a is b) # Compara si dos objetos son idénticos y no los valores en sí, por eso da False
print(a is not b)

# ----------------------------------

listaIn = [1, 2, 3, 4, 5]

print(3 in listaIn)
print(6 not in listaIn)
'''

# ======================================== CONDICIONALES ========================================

# if, if-else, if-elif-else

'''
personaA = 'Jorge'
personaB = 'Carlos'
personaC = 'María'
miEdad = 18

if (miEdad > 18): 
    print(personaA, 'es mi amigo')
elif (miEdad == 18): 
    print(personaB, 'es mi amigo')
else:
    print(personaC, 'es mi amigo')
'''

# ======================================== LISTAS ========================================

# lista, lista[x]
# append(x), insert(x,y), extend(x),
# pop(), del lista[x], remove(x)
# len(), reverse(), sort() 

'''
lista = []
listaNumeros = [1,2,3,4,5]
listaLetras = ['a','b','c','d','e']
listaMixta = [1, 'a', True, 3.14]

print(listaNumeros[0], listaLetras[1], listaMixta[2])

# ----------------------------------

listaMixta[2] = 'False'
print(listaMixta)

del listaMixta[2]
print(listaMixta)

# ------

listaNumeros.append(6)
print(listaNumeros)

print(listaNumeros.pop())

# ------

otraListaLetras = ['f', 'g']
listaLetras.extend(otraListaLetras)
print(listaLetras)

listaLetras.remove('g')
print(listaLetras)

# ------

listaMixta.insert(3, 3.33)
print(listaMixta)

# ----------------------------------

print(len(listaNumeros))

# ------

print(listaLetras)
listaLetras.reverse()
print(listaLetras)

# ------

listaLetras.sort()
print(listaLetras)

# ------

otraListaNumeros = [7, 8, 9]
listaConcatenada = listaNumeros + otraListaNumeros
print(listaConcatenada)

# ------

listaRepetida = ['a'] * 3
print(listaRepetida)
'''

# ======================================== TUPLAS ========================================

# Una TUPLA es una estructura de datos similar a una lista, pero inmutable. Esto significa que una vez que se crea una tupla, no se pueden modificar sus elementos.

'''
tupla = ('Francis', 25, 'Argentina') 

nombre, edad, pais = tupla # Desempaquetado / Desestructuración
print(nombre)
print(edad)
print(pais)
'''

# ======================================== CICLOS ========================================

# for-in, while, break, continue

'''
frutas = ["manzana", "banana", "frutilla"]
for fruta in frutas:
    print(fruta)

for i in range(3):
    print('for', i)

# ----------------------------------

contador = 0
while contador < 3:
    print('while', contador)
    contador += 1

contador = 0
while True:
    contador += 1
    if contador == 3:
        continue  # Salta esta iteración
    print('break/continue', contador)
    if contador == 5:
        break  # Sale del ciclo
'''

# ======================================== FUNCIONES ========================================

# Las funciones son bloques de código reutilizable que realizan una tarea específica.

'''
def nombreFuncion(parametro1, parametro2):
    resultado = parametro1 + parametro2
    return resultado

print(nombreFuncion(10, 2))

# ----------------------------------

def saludar(nombre = 'Mundo'): # Argumento por defecto
    print('Hola,', nombre)

saludar()
saludar('Francis')

# ----------------------------------

def suma(*args):
    total = 0

    for num in args:
        total += num
    return total

print(suma(20, 30, 50))
'''

# ======================================== EJERCICIO INTEGRADOR ========================================

'''
listaTuplas = []

def crearTuplaEnLista(nombre, edad):
    tupla = (nombre, edad)
    listaTuplas.append(tupla)

# Creando Tuplas
crearTuplaEnLista('Francis', 25)
crearTuplaEnLista('Nahuel', 10)
crearTuplaEnLista('Marco', 5)
print(listaTuplas)

# Ordenar Lista x Nombre / Ordenar Lista x Edad
listaTuplas.sort()
print(listaTuplas)

listaOrdenadaPorEdad = sorted(listaTuplas, key=lambda x: x[1])
print(listaOrdenadaPorEdad)
'''

# Hacer un ciclo que agregue a una lista los numeros del 1 al 10.
# Hacer una sumatoria de todos los numeros.
# Dividir la lista en dos listas: numeros pares e impares.
# Crear una funcion a la cual le agregues X parámetros del tipo string y los agregue a una lista. Además, utilizar otra función para devolver: el string más largo y la cantidad de caracteres de este último.

print('================================================')

listaNumeros = []

for i in range(10):
    listaNumeros.append(i+1)

print('Lista Números:', listaNumeros)

# -------------------------------------

totalSumatoria = 0

for i in listaNumeros:
    totalSumatoria += i
    
print('Sumatoria:',totalSumatoria)

# -------------------------------------

listaPar = []
listaImpar = []

for i in listaNumeros:
    nro = i
    i %= 2
    if (i == 0):
        listaPar.append(nro)
    else:
        listaImpar.append(nro)
        
print('Lista Par:', listaPar)
print('Lista Impar:', listaImpar)

# -------------------------------------

listaStrings = []

def functionString(*args):
    for arg in args:
        listaStrings.append(arg)
    print('Lista Strings:', listaStrings)

def stringMasLargo():
    string = ''
    longitud = 0
    for i in listaStrings:
        stringActual = i
        longitudStringActual = len(stringActual)
        if (longitudStringActual > longitud):
            string = stringActual
            longitud = longitudStringActual
    print('String más largo:', string)
    print('Cantidad de caracteres:', longitud)

functionString('Fran', 'Franco', 'Francis', 'Francisco', 'Franchesco')
stringMasLargo()

print('================================================')