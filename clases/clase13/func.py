# Archivo func.py
    # def listar_emple
    # def buscar_emple
    # def calcu_sueldo (Tener en cuenta: Tope semanal = 48hs, Valor hora = X, Horas extras = X)

from emple import *
from color import *

def listar_emple(): 
    for i in empleados:
        print(f'{green}{i}{reset}')

def buscar_emple(nombre):
    for i in empleados:
        if i['nombre'] == nombre:
            return i
    return None

def calcu_sueldo(nombre): 
    empleado = buscar_emple(nombre)

    if not empleado:
        return None

    empleadoSueldoFinal = empleado['sueldo']

    topeSemanal = 48
    valorHora = 100
    horasExtras = empleado['horas'] - topeSemanal

    if empleado['horas'] > topeSemanal:
        empleadoSueldoFinal = empleado['sueldo'] + (horasExtras * valorHora)

    return empleadoSueldoFinal