# Clase 12 - Repaso Funciones

# replace()
'''
def mi_replace(cadenaOriginal, subcadenaAReemplazar, subcadenaDeReemplazo):
    longitudAReemplazar = len(subcadenaAReemplazar)
    cadenaReemplazada = ''
    i = 0

    # mientras que i sea menor a la longitud de la cadena original...
    while i < len(cadenaOriginal):
        # si la subcadena entre el indice "i" y el indice "i + longitudAReemplazar" es igual a la subcadena a reemplazar...
        if cadenaOriginal[i:(i + longitudAReemplazar)] == subcadenaAReemplazar: 
            cadenaReemplazada += subcadenaDeReemplazo # guardo la subcadena en la nueva cadena
            i += longitudAReemplazar # omitimos la subcadena, llevando el puntero a la ultima letra de esta
        # de lo contrario, se guarda la letra a la cual se está apuntando, en la nueva cadena, y se pasa a la siguiente letra
        else:
            cadenaReemplazada += cadenaOriginal[i]
            i += 1

    return cadenaReemplazada

cadenaNueva = mi_replace('Hola, buenas tardes!', 'tardes!', 'noches!') # las mayusculas y minusculas, influyen
print('replace():', cadenaNueva)
'''

# find()
'''
def mi_find(cadena, subcadenaABuscar):
    longitudSubcadena = len(subcadenaABuscar)
    i = 0      

    while i < len(cadena):
        if cadena[i:(i + longitudSubcadena)] == subcadenaABuscar: 
            return i # me devuelve el índice de la primera letra, de la primera subcadena encontrada
        i += 1

    if i == len(cadena):
        return -1 # si la subcadena no existe en la cadena, se devuelve -1


print('find():', mi_find('Hola, quiero torta.', 'torta') ) # las mayusculas y minusculas, influyen
'''

# función de calcular porcentaje (valor, porcentaje)
'''
def calcular_porcentaje(valor, porcentaje):

    if valor < 0:
        return 'El valor debe ser no negativo.'
        #raise ValueError('El valor debe ser no negativo.')
    if not 0 < porcentaje <= 100:
        return 'Porcentaje inválido, debe estar entre 1 y 100.'
        #raise ValueError('Porcentaje inválido, debe estar entre 1 y 100.')

    calculo = (porcentaje * valor) / 100 # opcional: guardar el valor de la variable afuera para usarla después
    return calculo

print('calcular porcentaje:', calcular_porcentaje(1000, 20))
'''

# función de contar palabras
'''
def contar_palabras(cadena):
    contador = 1

    for i in cadena.strip():
        if i == ' ':
            contador += 1

    return contador

print('contar palabras:', contar_palabras('Hola, como va?'))
'''

# función de convertir moneda: dolar, euro, peso (moneda actual, cantidad, moneda a convertir)
'''
dolar = 1   # 1 dolar --> $880 ARS.
euro = 0.92 # 0.92 euros --> $880 ARS.
peso = 880  # $880 ARS --> 1 dolar y a 0.92 euros.

def convertir_moneda(monedaActual, cantidad, monedaAConvertir):

    listaMonedas = ['dolar', 'euro', 'peso']

    if monedaActual in listaMonedas:
        listaMonedas.remove(monedaActual)
    else:
        return 'Tipo de moneda actual inválida.'
    
    if not cantidad >= 0:
        return 'La cantidad no puede ser negativa.'
    
    if monedaAConvertir not in listaMonedas:
        return 'Tipo de moneda a convertir inválida.'

    conversion = 0

    if monedaActual == 'dolar' and monedaAConvertir == 'euro':
        conversion = cantidad * euro
    elif monedaActual == 'dolar' and monedaAConvertir == 'peso':
        conversion = cantidad * peso

    elif monedaActual == 'euro' and monedaAConvertir == 'dolar':
        conversion = cantidad / euro
    elif monedaActual == 'euro' and monedaAConvertir == 'peso':
        conversion = (cantidad * peso) / euro # regla de 3

    elif monedaActual == 'peso' and monedaAConvertir == 'dolar':
        conversion = cantidad / peso
    elif monedaActual == 'peso' and monedaAConvertir == 'euro':
        conversion = (cantidad * euro) / peso # regla de 3

    return round(conversion, 5)

print('cambiar moneda:', convertir_moneda('euro', 1, 'peso'))
'''

# Pensar en la aplicación de predicción, similar al de "el gato y la caja".

# Calculadora (+, -, /, *)
# La función calcular(valor1, valor2, operacion) debe devolver un resultado
'''
def calcular(valor1,valor2,op):

    listaOperadores = ['+','-','/','*']

    # Validación 1: si valor1 y valor2 no son números, devolver error
    if not isinstance(valor1, (int, float)) or not isinstance(valor2, (int, float)):
        return 'Error. Por favor, ingresa números válidos.'
    
    # Validación 2: si op no es un operador, devolver error
    if op not in listaOperadores:
        return 'Error. Por favor, ingresa un operador válido.'

    # Resolver cálcuclo y retornar
    if op == '+':
        return round(valor1 + valor2, 3)
    elif op == '-':
        return round(valor1 - valor2, 3)
    elif op == '/':
        if valor2 == 0:
            return 'Error. Por favor, no dividir por cero.'
        return round(valor1 / valor2, 3)
    elif op == '*':
        return round(valor1 * valor2, 3)

print(f'Calculadora simple: {calcular(10,2,'*')}')
'''

# Para el siguiente ejercicio, tener en cuenta:
# isupper(), islower(), isnumeric(), isdigit()

# Login: validar usuario y contraseña. 
# def validar_user(cadena), el usuario debe contener más de 6 caracteres y ningún número
# def validar_pass(cadena), la contraseña debe contener 1 mayúscula, 1 minúscula, 1 número y más de 12 caracteres

def validar_user(cadena):

    if len(cadena) > 6:
        for i in cadena:
            if i.isnumeric():
                return False
        return True
    else:
        return False

username = input ('Ingrese el nombre de usuario: ').strip()
print(validar_user(username))

def validar_pass(cadena):
    hayMayus = False
    hayMinus = False
    hayNumero = False

    if len(cadena) > 12:
        for i in cadena:
            if i.isnumeric():
                hayNumero = True
                #print('Hay un numero')
            elif i.isupper():
                hayMayus = True
                #print('Hay un upper')
            elif i.islower():
                hayMinus = True
                #print('Hay un lower')
        if hayMayus and hayMinus and hayNumero:
            return True
        return False
    else:
        return False

password = input ('Ingrese la contraseña: ').strip()
print(validar_pass(password))