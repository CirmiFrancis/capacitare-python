# Piedra Papel Tijera

import random

print('¿Piedra, Papel o Tijera?')

jugadaUsuario = input('Tu jugada es: ')
# print(type(jugadaUsuario))

listaJugadas = ['Piedra', 'Papel', 'Tijera']
jugadaIA = random.choice(listaJugadas)

print('La IA jugó: ' + jugadaIA)
# print(type(jugadaIA))
    
resultado = ''

if jugadaUsuario == jugadaIA:
    resultado = 'Nadie. Empate'
elif (jugadaUsuario=='Piedra' and jugadaIA=='Tijera') or \
     (jugadaUsuario=='Papel' and jugadaIA=='Piedra') or \
     (jugadaUsuario=='Tijera' and jugadaIA=='Papel'):
    resultado = 'Usuario'
else:
    resultado = 'IA'

print('El ganador es... ' + resultado)