# Clase 11 - Generar Ejecutable & Funciones

# ======================== GENERAR EJECUTABLE ========================

# "PyInstaller" permite convertir scripts en ejecutables.

# Para instalar "PyInstaller" y verificar la versión, escribo los siguientes comandos:
# pip3 install pyinstaller
# pip3 --version

# En la terminal, escribo "ls" y "cd nombredeldirectorio" para ir hacia la dirección donde está el archivo a compilar.

# Para generar el ejecutable de un script, escribo el siguiente comando:
# pyinstaller --onefile nombredelarchivo.py

# ======================== FUNCIONES ========================

'''
nombre = input('Ingrese su nombre: ')

def saludar(nombre):
    print('Hola', nombre)

saludar(nombre)
'''

# len()
'''
cadena = input('Ingresa una cadena de caracteres: ')

def mi_len(parametro):
    cont = 0
    for i in parametro:
        cont += 1
    return cont

print('len():', mi_len(cadena))
'''

# isnumeric()
'''
cadena = input('Ingresa una cadena de caracteres: ')

def mi_isnumeric(parametro):
    nros = ['0','1','2','3','4','5','6','7','8','9','.']
    lon = 0

    for i in parametro:
        if i not in nros:
            return False
        else:
            lon += 1
    
    if lon == len(parametro):
        return True
    else:
        return False

print('isnumeric():', mi_isnumeric(cadena))
'''

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

    calculo = (porcentaje * valor) / 100
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

# aplicación de predicción, similar al de "el gato y la caja"
# https://elgatoylacaja.com/elnudo/el-juego-de-la-prediccion?utm_source=sitioEGLC&utm_medium=gato-hoy