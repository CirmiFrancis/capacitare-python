# Piedra Papel Tijera

import random

print('¿Piedra, Papel o Tijera?')

jugadaUsuario = input('Tu jugada es: ')
# print(type(jugadaUsuario))

listaJugadas = ['Piedra', 'Papel', 'Tijera']
jugadaIA = random.choice(listaJugadas)

print('La IA jugó: ' + jugadaIA)
# print(type(jugadaIA))
    
ganador = ''

if jugadaUsuario=='Piedra' and jugadaIA=='Tijera':
    ganador = 'Usuario'
elif jugadaUsuario=='Piedra' and jugadaIA=='Papel':
    ganador = 'IA'
elif jugadaUsuario=='Piedra' and jugadaIA=='Piedra':
    ganador = 'Nadie. Empate'

if jugadaUsuario=='Papel' and jugadaIA=='Piedra':
    ganador = 'Usuario'
elif jugadaUsuario=='Papel' and jugadaIA=='Tijera':
    ganador = 'IA'
elif jugadaUsuario=='Papel' and jugadaIA=='Papel':
    ganador = 'Nadie. Empate'

if jugadaUsuario=='Tijera' and jugadaIA=='Papel':
    ganador = 'Usuario'
elif jugadaUsuario=='Tijera' and jugadaIA=='Piedra':
    ganador = 'IA'
elif jugadaUsuario=='Tijera' and jugadaIA=='Tijera':
    ganador = 'Nadie. Empate'

print('El ganador es... ' + ganador)
