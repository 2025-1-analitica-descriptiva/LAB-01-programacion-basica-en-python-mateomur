"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """ 
    resultado_dict = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            if len(columnas) >= 5:
                codigos = columnas[4].split(',')
                for par in codigos:
                    clave, valor_str = par.split(':')
                    valor = int(valor_str)

                    if clave in resultado_dict:
                        resultado_dict[clave][0] = min(resultado_dict[clave][0], valor)
                        resultado_dict[clave][1] = max(resultado_dict[clave][1], valor)
                    else:
                        resultado_dict[clave] = [valor, valor]

    resultado = [(clave, valores[0], valores[1]) for clave, valores in resultado_dict.items()]
    resultado.sort(key=lambda x: x[0])
    return resultado

