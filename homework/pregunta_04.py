def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    
    conteo_meses = {}
    
   
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            if len(columnas) >= 3:
                fecha = columnas[2]
                mes = fecha.split('-')[1]
                
                if mes in conteo_meses:
                    conteo_meses[mes] += 1
                else:
                    conteo_meses[mes] = 1
    

    resultado = [(mes, cantidad) for mes, cantidad in conteo_meses.items()]
    

    resultado.sort(key=lambda x: x[0])
    
    return resultado