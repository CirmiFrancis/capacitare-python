# Aplicación de predicción, similar al de "el gato y la caja".
# https://elgatoylacaja.com/elnudo/el-juego-de-la-prediccion?utm_source=sitioEGLC&utm_medium=gato-hoy

# Explicación sencilla de como funciona la IA:
# Las primeras 4 jugadas son aleatorias. Luego, se tienen en cuenta las últimas 4 jugadas del usuario y el historial de jugadas, dividido en sub-arrays de 4 elementos. Es decir, la IA va a realizar una jugada dependiendo de tus últimas 4 jugadas, pero cada 4ta jugada, cuando previamente se completó un sub-array, la IA realiza una jugada basándose en la jugada más común del usuario en cada sub-array. 

# Ejemplo historial:        [ 'i','d','d','i','i','i','d','d','d','i' ]     (10)
# Ejemplo subhistorial:     [ ['i','d','d','i'], ['i','i','d','d'] ]        (2x4)
# Ejemplo reciente:         [ 'd','d','d','i' ]                             (4)

# Imports
import random

# Colores
red = "\033[91m"
green = '\033[92m'
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

# Variables Globales
jugadasPosibles = ['i', 'd'] # jugadas posibles, i = izquierda o d = derecha
historialJugadas = [] # historial total de jugadas
subHistorialJugadas = [] # historial parcial de jugadas, divididas en sub-arrays de 4 elementos
historialRecienteJugadas = [] # ultimas 4 jugadas
contadorRondas = 1 # ronda actual
puntosMaximo = 50 # cantidad de rondas
puntosUsuario = 0 # rondas ganadas por usuario
puntosIA = 0 # rondas ganadas por IA

# Reglas
def dar_reglas():
# Funcion que se utiliza únicamente al inicio de la partida. Imprime las reglas del juego.
    print('=============================================================')
    print(f'{yellow}1) Evita que la IA anticipe tu jugada{reset}')
    print(f'{yellow}2) Tienes dos opciones: I (izquierda) o D (derecha){reset}')
    print(f'{yellow}3) El primero en alcanzar los {puntosMaximo} puntos, gana{reset}')
    print(f'\n{yellow}¿Podrás ganarle a la IA? ¡Suerte!{reset}')

# Jugada Usuario
def jugada_usuario():
# El usuario ingresa una jugada. Si esta jugada esta en jugadasPosibles, se guarda el valor en el historial y se retorna. De lo contrario, y si la jugada tampoco es /historial, /subhistorial, /reciente o !help, simplemente devuelve un mensaje y el jugador debe volver a ingresar una jugada.
    jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower() # el usuario ingresa su jugada ('i' o 'd')

    while jugadaUsuario not in jugadasPosibles: # si la jugada no es ni 'i' o 'd', ...
        if jugadaUsuario == '/historial':
            print(historialJugadas) # imprime todas las jugadas del usuario
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        elif jugadaUsuario == '/subhistorial':
            print(subHistorialJugadas) # imprime las jugadas del usuario, divididas en arrays de 4 elementos
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        elif jugadaUsuario == '/reciente':
            print(historialRecienteJugadas) # imprime las ultimas 4 jugadas del usuario
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        elif jugadaUsuario == '!help': # imprime los distintos comandos
            print(f'{green}/historial{reset} para ver todas las jugadas que hiciste hasta el momento.')
            print(f'{green}/subhistorial{reset} para ver las jugadas que hiciste, divididas en arrays de 4 elementos.')
            print(f'{green}/reciente{reset} para ver las últimas 4 jugadas realizadas.')
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        else:
            print(f'{yellow}Jugada inválida. Por favor, escribe nuevamente.{reset}\n')
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()

    historialJugadas.append(jugadaUsuario) # si la jugada es 'i' o 'd', se guarda en el historial
    return jugadaUsuario # retorna el valor de la jugada del usuario

# Jugada IA
def jugada_ia():
# Las primeras 4 jugadas, la IA juega aleatoriamente, guardando en la 4ta jugada el primer subhistorial y el historial de jugadas reciente. Luego, siempre se tiene en cuenta las jugadas recientes y cada 4 jugadas prioriza la jugada que más realizó el usuario en cada sub-array.
    global historialRecienteJugadas, subHistorialJugadas, historialRecienteJugadas

    if len(historialJugadas) <= 4:
        jugadaIA = jugadasPosibles[random.randrange(2)] #random.choice(jugadasPosibles)
        if len(historialJugadas) % 4 == 0:
            subHistorialJugadas.append(historialJugadas[:4]) 
            historialRecienteJugadas = historialJugadas[:4]
    else:
        historialRecienteJugadas = historialJugadas[-4:] # historialJugadas[ (len(historialJugadas) - 4):]
        if len(historialJugadas) % 4 == 0:
            subHistorialJugadas.append(historialRecienteJugadas)
        jugadaIA = opcion_mas_elegida_por_usuario_en_cada_subarray()
        
    print(f'{red}IA:{reset}', jugadaIA)
    return jugadaIA

def opcion_mas_elegida_por_usuario_en_cada_subarray(): 
# En esta funcion, si la cantidad de jugadas realizadas es divisible por 4 (es decir, cada 4 jugadas), se recorre el array subHistorialJugadas, el cual contiene como elementos sub-arrays, es decir, arrays dentro de un array. Dentro de cada sub-array, se compara si la jugada mas elegida por el usuario es igual a 'i', en ese caso se suma al contadorI, de lo contrario, se suma al contadorD. Luego, se compara contadorI y contadorD y dependiendo de quien es mayor, igual o menor, se realiza una jugada u otra. De lo contrario, se tiene en cuenta la opcion mas elegida en las jugadas recientes del usuario.
# En resumen: cada 4 jugadas, se identifica, en cada una de las sub-arrays, cual fue la jugada mas elegida EN CADA sub-array, y dependiendo de eso, la IA elige una u otra jugada. De lo contrario, se tiene en cuenta la opcion mas elegida en las jugadas recientes del usuario.
    contadorI = 0
    contadorD = 0

    if len(historialJugadas) % 4 == 0:
        for i in subHistorialJugadas:
            if opcion_mas_elegida_por_usuario(i) == 'i':
                contadorI += 1
            else:
                contadorD += 1
    
        if contadorI > contadorD:
            return 'i'
        elif contadorI < contadorD:
            return 'd'
        elif contadorI == contadorD:
            return jugadasPosibles[random.randrange(2)]
    else:
        jugadaIA = opcion_mas_elegida_por_usuario(historialRecienteJugadas)
        return jugadaIA

def opcion_mas_elegida_por_usuario(array):
# Esta funcion tiene como parametro un array, sobre el cual se cuentan y se guardan las jugadas 'i' y las jugadas 'd', para luego compararlas y retornar una jugada u otra, la cual será usada por la IA.
    contadorI = array.count('i')
    contadorD = array.count('d')

    # for i in array:
    #     if i == 'i':
    #         contadorI += 1
    #     else:
    #         contadorD += 1

    if contadorI > contadorD:
        return 'i'
    elif contadorI < contadorD:
        return 'd'
    else:
        return jugadasPosibles[random.randrange(2)]

# Comparar Jugadas
def comparar_jugadas(jugadaUsuario, jugadaIA):
# Si las jugadas son IGUALES, suma un punto la IA, sino, suma un punto el usuario.
    global puntosUsuario, puntosIA

    if jugadaUsuario != jugadaIA:
        puntosUsuario += 1 
    elif jugadaUsuario == jugadaIA:
        puntosIA += 1

# Dar Resultado
def dar_resultado():
# Funcion que se utiliza únicamente al final de la partida, cuando ya hay un ganador. Imprime el resultado con el ganador.
    print('=============================================================')
    print(f'{yellow}- RESULTADO -{reset}\n')
    print(f'{blue}Tú ({puntosUsuario}){reset} - {red}IA ({puntosIA}){reset}')

    if puntosUsuario > puntosIA:
        print(f'\n{yellow}Ganaste.{reset}')
    else:
        print(f'\n{yellow}Perdiste.{reset}')

# Programa Principal
# Imprimimos las reglas, comenzamos un ciclo donde el usuario y la IA van a jugar, y al finalizar se imprime el resultado.
dar_reglas()

while puntosUsuario < puntosMaximo and puntosIA < puntosMaximo:
    print('=============================================================')
    print(f'{yellow}- RONDA {contadorRondas} -{reset} (Escribe {green}!help{reset} para ver todos los comandos.)\n')

    # print(f'{yellow}historialJugadas: {historialJugadas}{reset}\n')
    # print(f'{yellow}subHistorialJugadas: {subHistorialJugadas}{reset}\n')
    # print(f'{yellow}historialRecienteJugadas: {historialRecienteJugadas}{reset}\n')

    print(f'{blue}Tú ({puntosUsuario}){reset} - {red}IA ({puntosIA}){reset}\n')
    jugadaUsuario = jugada_usuario()
    jugadaIA = jugada_ia()
    comparar_jugadas(jugadaUsuario, jugadaIA)
    contadorRondas += 1

dar_resultado()
print('=============================================================')