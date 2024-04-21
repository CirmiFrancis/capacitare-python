#Ta Te Ti

jugadasDisponibles = [1,2,3,4,5,6,7,8,9]
#print(jugadasDisponibles)

def imprimirTablero():
    print('')
    print(f' {jugadasDisponibles[0]} || {jugadasDisponibles[1]} || {jugadasDisponibles[2]} ')
    print('=============')
    print(f' {jugadasDisponibles[3]} || {jugadasDisponibles[4]} || {jugadasDisponibles[5]} ')
    print('=============')
    print(f' {jugadasDisponibles[6]} || {jugadasDisponibles[7]} || {jugadasDisponibles[8]} ')
    print('')

imprimirTablero()

jugada = int( input('Elige una posición: ') )

if jugada in jugadasDisponibles:
    jugadasDisponibles[jugada - 1] = 'X'
    imprimirTablero()
else:
    print('Jugada incorrecta')
    print(jugadasDisponibles)
