# Piedra - Papel - Tijera
import random

bool = True
listaJugadas = ['Piedra', 'Papel', 'Tijera'] 
resultado = ''
victoriasUsuario = 0
victoriasIA = 0

while True:
    # Iniciar Juego
    print('===================================')
    print('¿Piedra - Papel - Tijera? (Fin para salir)')
    print('')

    # Jugada Usuario
    while True:
        jugadaUsuario = input()
        jugadaUsuario = jugadaUsuario.strip().capitalize()

        if jugadaUsuario == 'Fin': 
            bool = False
            break
        elif (jugadaUsuario not in listaJugadas):
            print('Jugada no válida. Por favor, vuelve a escribir tu jugada.')
            print('===================================')
        else:
            break

    # Finalizar Ejecución
    if not bool: 
        print('===================================')
        break

    # Jugada IA
    jugadaIA = random.choice(listaJugadas)

    # Mostrar Jugadas
    print('')
    print('(Tú)', jugadaUsuario)
    print('(IA)', jugadaIA)
    print('')
        
    # Comparar Jugadas
    if jugadaUsuario == jugadaIA:
        resultado = 'Empate'
    elif(jugadaUsuario == 'Piedra' and jugadaIA == 'Tijera') or \
        (jugadaUsuario == 'Papel'  and jugadaIA == 'Piedra') or \
        (jugadaUsuario == 'Tijera' and jugadaIA == 'Papel'):
        resultado = 'Ganaste'
        victoriasUsuario += 1
    else:
        resultado = 'Perdiste'
        victoriasIA += 1

    # Mostrar Resultado
    resultado = f'Resultado: {resultado} ({victoriasUsuario} - {victoriasIA})'
    print(resultado)