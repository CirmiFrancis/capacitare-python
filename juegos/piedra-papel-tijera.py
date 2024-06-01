# Piedra - Papel - Tijera
import random

# Colores
red = "\033[91m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

# Variables
booleano = True
listaJugadas = ['Piedra', 'Papel', 'Tijera'] 
resultado = ''
victoriasUsuario = 0
victoriasIA = 0

# Iniciar Ejecución
while True:
    # Iniciar Juego
    print('===================================')
    print(f'{yellow}¿Piedra - Papel - Tijera?{reset} (Fin para salir)')
    print('')

    # Jugada Usuario
    while True:
        jugadaUsuario = input()
        jugadaUsuario = jugadaUsuario.strip().capitalize()

        if jugadaUsuario == 'Fin': 
            booleano = False
            break
        elif (jugadaUsuario not in listaJugadas):
            print(f'{red}Jugada no válida. Por favor, vuelve a escribir tu jugada.{reset}')
        else:
            break

    # Finalizar Ejecución
    if not booleano: 
        print('===================================')
        break

    # Jugada IA
    jugadaIA = random.choice(listaJugadas)

    # Mostrar Jugadas
    print(f'\n{blue}(TÚ) {jugadaUsuario}{reset}')
    print(f'{red}(IA) {jugadaIA}{reset}\n')
        
    # Comparar Jugadas
    if jugadaUsuario == jugadaIA:
        print('Empate')
    elif(jugadaUsuario == 'Piedra' and jugadaIA == 'Tijera') or \
        (jugadaUsuario == 'Papel'  and jugadaIA == 'Piedra') or \
        (jugadaUsuario == 'Tijera' and jugadaIA == 'Papel'):
        print('Ganaste')
        victoriasUsuario += 1
    else:
        print('Perdiste')
        victoriasIA += 1

    # Mostrar Resultado
    print (f'{yellow}Resultado:{reset} {blue}{victoriasUsuario}{reset} - {red}{victoriasIA}{reset}')
    print(resultado)