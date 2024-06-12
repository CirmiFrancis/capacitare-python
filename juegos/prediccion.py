# Aplicación de predicción, similar al de "el gato y la caja".
# https://elgatoylacaja.com/elnudo/el-juego-de-la-prediccion?utm_source=sitioEGLC&utm_medium=gato-hoy

# Colores
red = "\033[91m"
green = '\033[92m'
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

# Variables Globales
jugadasPosibles = ['izquierda', 'derecha']
historialJugadas = []
contadorRondas = 1
puntosUsuario = 0
puntosIA = 0
puntosMaximo = 10

# Reglas
def dar_reglas():
    print('=============================================================')
    print(f'{yellow}1) Evita que la IA anticipe tu jugada{reset}')
    print(f'{yellow}2) Tienes dos opciones: IZQUIERDA o DERECHA{reset}')
    print(f'{yellow}3) El primero en alcanzar los 10 puntos, gana{reset}')
    print(f'\n{yellow}¿Podrás ganarle a la IA? ¡Suerte!{reset}')

# Jugada Usuario
def jugada_usuario():
    jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()

    while jugadaUsuario not in jugadasPosibles:
        if jugadaUsuario == '/historial':
            print(historialJugadas) # imprime todas las jugadas del usuario
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()
        else:
            print(f'{yellow}Jugada inválida. Por favor, escribe nuevamente.{reset}\n')
            jugadaUsuario = input(f'{blue}Tú: {reset}').strip().lower()

    historialJugadas.append(jugadaUsuario)
    return jugadaUsuario

# Jugada IA
def jugada_ia():
    import random

    jugadaIA = jugadasPosibles[random.randrange(2)]
    print(f'{red}IA:{reset}', jugadaIA)

    # if len(historialJugadas) < 4:
    #     jugadaIA = jugadasPosibles[random.randrange(2)]
    #     print(f'{red}IA:{reset}', jugadaIA)
    # else:
    #     jugadaIA = posibles_jugadas(historialJugadas)
    #     if jugadaIA == None:
    #         #print(f'{yellow}jugadaIA == None{reset}')
    #         jugadaIA = jugadasPosibles[random.randrange(2)]
    #     print(f'{red}IA:{reset}', jugadaIA)
    return jugadaIA

# def posibles_jugadas(jugadas):
#     if jugadas[-3:-1] == ['izquierda', 'izquierda']:
#         #print(f'{yellow}primera jugada{reset}')
#         return 'izquierda'
#     if jugadas[-3:-1] == ['derecha', 'derecha']:
#         #print(f'{yellow}segunda jugada{reset}')
#         return 'derecha'
#     if jugadas[-4:-1] == ['izquierda', 'derecha', 'izquierda']:
#         #print(f'{yellow}tercera jugada{reset}')
#         return 'derecha'
#     if jugadas[-4:-1] == ['derecha', 'izquierda', 'derecha']:
#         #print(f'{yellow}cuarta jugada{reset}')
#         return 'izquierda'

# Comparar Jugadas
def comparar_jugadas(jugadaUsuario, jugadaIA):
    global puntosUsuario, puntosIA

    if jugadaUsuario != jugadaIA:
        puntosUsuario += 1 
    elif jugadaUsuario == jugadaIA:
        puntosIA += 1

# Dar Resultado
def dar_resultado():
    print('=============================================================')
    print(f'{yellow}- RESULTADO -{reset}\n')
    print(f'{blue}Tú ({puntosUsuario}){reset} - {red}IA ({puntosIA}){reset}')

    if puntosUsuario > puntosIA:
        print(f'\n{yellow}Ganaste.{reset}')
    else:
        print(f'\n{yellow}Perdiste.{reset}')

# Programa Principal
dar_reglas()

while puntosUsuario < puntosMaximo and puntosIA < puntosMaximo:
    print('=============================================================')
    print(f'{yellow}- RONDA {contadorRondas} -{reset} (Escribe {green}/historial{reset} para ver todas las jugadas que hiciste hasta el momento.)\n')
    print(f'{blue}Tú ({puntosUsuario}){reset} - {red}IA ({puntosIA}){reset}\n')
    jugadaUsuario = jugada_usuario()
    jugadaIA = jugada_ia()
    comparar_jugadas(jugadaUsuario, jugadaIA)
    contadorRondas += 1

dar_resultado()
print('=============================================================')