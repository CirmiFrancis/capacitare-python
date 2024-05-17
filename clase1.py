# Clase 1 - Variables & Print

# Para correr el codigo: 'python3 clase1.py'

# ======================================== CÓDIGO 1 ========================================

# edad = 0

# print('Python')
# print(edad)
# print(type(edad))

# edad = int(input('Ingrese su edad: '))

# #Casteo explicíto: le decimos que tome a la variable 'edad' como un string
# print('Tu edad es: ' + str(edad))
# print('Tu edad es:', edad)

# ======================================== CÓDIGO 2 ========================================

# nombre = input('Ingrese su nombre: ')

# print('Hola '+nombre)

# ======================================== CÓDIGO 3 ========================================

nota1 = 0
nota2 = 0
nota3 = 0
promedio = 0

nota1 = int(input('Ingrese la primera nota: '))
nota2 = int(input('Ingrese la segunda nota: '))
nota3 = int(input('Ingrese la tercera nota: '))
promedio = (nota1+nota2+nota3) / 3

print(promedio)