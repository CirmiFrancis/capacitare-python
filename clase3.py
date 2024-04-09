# Clase 3

# Repaso Clase 2
'''
 replace(), reemplaza una cadena de strings por otra
 find(), para encontrar un parámetro
 len(), calula la cantidad
 strip(), elimina los espacios blancos
 upper(), a mayuscula
 lower(), a minuscula
 capitalize(), primera letra mayuscula
 split(), divide una cadena
 join(), une cadenas
 count(), devuelve el nro de veces que aparece una subcadena
'''

# Ejercicio 1
'''
cadena1 = input('Ingresa una cadena: ')
cadena2 = input('Ingresa otra cadena: ')

suma = len(cadena1) + len(cadena2)
print(suma)
'''

# Ejercicio 2
'''
cadena = input('Escribe una cadena: ')
buscar = input('Escribe una palabra que esté contenida en la cadena: ')

indice = cadena.find(buscar)
print (indice)
'''

# Ejercicio 3
'''
palabra = input('Escribe una palabra con al menos una mayuscula y una minuscula: ')

print (palabra)
print (palabra.upper())
print (palabra.lower())
'''

# Ejercicio 4
'''
frase = input('Escribe una frase con espacios en blanco: ')
caracter1 = input('Un caracter: ')
caracter2 = input('Otro caracter: ')

nuevaFrase = frase.strip().replace(caracter1, caracter2)

print(nuevaFrase)
'''

# Condicionales

#If - Else - Elif
'''    
edad = int( input('Ingresar edad: ') )
    
if edad > 18:
    print('Es mayor')
elif edad==18:
    print('Tiene 18 años')
else:
    print('Es menor')
'''

# Ejercicio Contraseña
'''
password = '1234'
ingreso = input('Ingresar Contraseña: ')

if password==ingreso:
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')
'''

bool = True

while bool:
    password = input('Ingresar Contraseña: ')
    
    if len(password) >= 12:
        print('Contraseña fuerte. Tiene 12 o más caracteres.')
        bool = False
    else:
        print('Contraseña débil. Tiene menos de 12 caracteres.')
