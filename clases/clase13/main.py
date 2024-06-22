from func import *
from emple import *
from color import *

def main():
    flag = True

    while flag:
        print(f'\n{yellow}============================================================={reset}\n')
        print(f'{yellow}COMANDOS:{reset} (Escribe {red}FIN{reset} para salir.)\n')
        print('1. Lista Empleados')
        print('2. Buscar Empleado')
        print('3. Calcular Sueldo\n')

        comando = input(f'{yellow}Ingrese el número del comando que quiera ejecutar: {reset}').strip().upper()

        if comando == 'FIN':
            print(f'\n{yellow}============================================================={reset}\n')
            flag = False
            break

        elif comando == '1':
            listar_emple()
        elif comando == '2':
            nombre = input(f'{yellow}Ingrese el nombre del empleado: {reset}').strip().capitalize()
            print(f'{green}{buscar_emple(nombre)}{reset}')
        elif comando == '3':
            nombre = input(f'{yellow}Ingrese el nombre del empleado: {reset}').strip().capitalize()
            print(f'{green}{calcu_sueldo(nombre)}{reset}')
            
        else:
            print('Error. Ingrese un número de comando correcto.')
main()

# listar_emple()

# print( buscar_emple('Francis') )
# print( buscar_emple('Lionel') )
# print( buscar_emple('Ángel') )
# print( buscar_emple('Rodrigo') )
# print( buscar_emple('Alexis') )

# print( calcu_sueldo('Francis') )
# print( calcu_sueldo('Lionel') )
# print( calcu_sueldo('Ángel') )
# print( calcu_sueldo('Rodrigo') )
# print( calcu_sueldo('Alexis') )