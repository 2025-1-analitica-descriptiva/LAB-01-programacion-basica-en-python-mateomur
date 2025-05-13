"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv') as archivo:
        max_min = {}
        for line in archivo:
            columnas = line.strip().split('\t')
            if columnas:
                letra = columnas[0]
                valor = int(columnas[1])
                if letra in max_min:
                    max_min[letra][0] = max(max_min[letra][0], valor)
                    max_min[letra][1] = min(max_min[letra][1], valor)
                else:
                    max_min[letra] = [valor, valor]
    resultado = [(letra, max_valor, min_valor) for letra, (max_valor, min_valor) in max_min.items()]
    resultado.sort(key=lambda x: x[0])
    print(max_min)
    return resultado


if __name__ == "__main__":
    print(pregunta_05())


