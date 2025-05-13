"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():

    suma = 0
    with open("files/input/data.csv", "r")  as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            if len(columnas) >= 2:
                suma += int(columnas[1])
    return suma
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
