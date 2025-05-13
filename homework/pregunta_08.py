"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_08():
    
    agrupados = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            letra = columnas[0]               
            numero = int(columnas[1])      

            if numero in agrupados:
                agrupados[numero].add(letra)
            else:
                agrupados[numero] = {letra}

    resultado = []
    for numero, letras in agrupados.items():
        letras_ordenadas = sorted(letras)
        resultado.append((numero, letras_ordenadas))

    resultado.sort(key=lambda x: x[0])
    return resultado
