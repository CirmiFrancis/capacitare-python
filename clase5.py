# Ejercicio 1 - Temperatura

'''
tipoTemperatura = input('Elige el tipo de temperatura: ').lower().strip()

if tipoTemperatura == 'celsius': 
    temperaturaCelsius = float( input('Ingresa la temperatura en Celsius: ') )
    temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32
    print(f'Fahrenheit: {temperaturaFahrenheit}' )
elif tipoTemperatura == 'fahrenheit':
    temperaturaFahrenheit = float(  input('Ingresa la temperatura en Fahrenheit: ') )
    temperaturaCelsius = (temperaturaFahrenheit - 32) * 5/9
    print(f'Celsius: {temperaturaCelsius}' )
else:
    print('Error. Tipo de temperatura incorrecta.')
'''

# Ejercicio 2 - Área Figura Geométrica

'''
figura = input('Elegir una figura geométrica: ').lower().strip()

if figura == 'rectangulo':
    base = float( input('Escribir una base: ') )
    altura = float( input('Escribir una altura: ') )
    area = base * altura
elif figura == 'triangulo':
    base = float( input('Escribir una base: ') )
    altura = float( input('Escribir una altura: ') )
    area = (base * altura) / 2
elif figura == 'circulo':
    radio = float( input('Escribir un radio: ') )
    pi = 3.14
    area = pi * radio ** 2  
else:
    print('Error. Figura geométrica incorrecta.')
    
print(f'El área del {figura} es {area}')
'''

# Ejercicio 3 - Conversión Moneda

'''
dolar = 1
euro = 0.94
peso = 871

monedaOrigen = input('Ingresa el tipo de moneda de origen: ').lower().strip()
monedaDestino = input('Ingresa el tipo de moneda de destino: ').lower().strip()
monto = float( input('Ingresa el monto: ') )

if monedaOrigen == 'dolar' and monedaDestino == 'euro':
    conversion = monto * euro
elif monedaOrigen == 'dolar' and monedaDestino == 'peso':
    conversion = monto * peso
elif monedaOrigen == 'euro' and monedaDestino == 'peso':
    conversion = monto * (peso / euro)
elif monedaOrigen == 'euro' and monedaDestino == 'dolar':
    conversion = monto / euro
elif monedaOrigen == 'peso' and monedaDestino == 'dolar':
    conversion = monto / peso
elif monedaOrigen == 'peso' and monedaDestino == 'euro':
    conversion = monto / (peso / euro)
else:
    print('Error. Tipo de monedas incorrectas.')

print(f'El valor de conversión es: {conversion}')
'''

# Ciclos
## Tipos: for-in, while, break, continue

'''
frutas = ["manzana", "banana", "frutilla"]
for fruta in frutas:
    print(fruta)
    
print('----------------------------------')

for i in range(3):
    print('for', i)

print('----------------------------------')

contador = 0
while contador < 3:
    print('while', contador)
    contador += 1

print('----------------------------------')

contador = 0
while True:
    contador += 1
    if contador == 3:
        continue  # Salta esta iteración
    print('break/continue', contador)
    if contador == 5:
        break  # Sale del ciclo
'''

# Ejercicio 4

'''
flag = True

while flag == True:
    figura = input('Elegir una figura geométrica: ').lower().strip()

    if figura == 'rectangulo':
        base = float( input('Escribir una base: ') )
        altura = float( input('Escribir una altura: ') )
        area = base * altura
    elif figura == 'triangulo':
        base = float( input('Escribir una base: ') )
        altura = float( input('Escribir una altura: ') )
        area = (base * altura) / 2
    elif figura == 'circulo':
        radio = float( input('Escribir un radio: ') )
        pi = 3.14
        area = pi * radio ** 2  
    else:
        print('Error. Figura geométrica incorrecta.')
    
    print(f'El área del {figura} es {area}')
    
    set = input('¿Seguir? ').lower().strip()
    
    if set == 'no':
        flag = False
'''

# Ejercicio 5
# Pedir un nro al usuario e imprimir la tabla de multiplicacion del 1 al 10 de ese nro

nro = int( input('Elige un nro: ') )
i = 1

while i < 11:
    print(nro*i)
    i += 1
