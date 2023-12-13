import re
import json

categorias = ["U12-M","U12-F","U14-M","U14-F","U16-M","U16-F","U17-M","U17-F","U18-M","U18-F","U20-M","U20-F","U23-M","U23-F","MAYORES-M","MAYORES-F",]

def guardarJsonVariables(variables_torneo):
    print(variables_torneo)

    nombre_torneo = variables_torneo[0]
    fecha_torneo = variables_torneo[1]
    siglaslugar_torneo = variables_torneo[2]
    pais_torneo = variables_torneo[3]
    organiza_torneo = variables_torneo[4]
    fiscaliza_torneo = variables_torneo[5]

    datos_torneo = {
        "nombre": nombre_torneo,
        "fecha-inicio": fecha_torneo[0],
        "fecha-fin": fecha_torneo[1],
        "siglas-lugar": siglaslugar_torneo,
        "pais": pais_torneo,
        "organiza": organiza_torneo,
        "fiscaliza": fiscaliza_torneo,
    }
    try:
        with open('torneos.json', 'r+') as archivo:
            # Leer datos existentes
            json_torneo = json.load(archivo)

            # Verificar si el torneo ya existe en el JSON
            if nombre_torneo in json_torneo.get("torneos", {}):
                if json_torneo["torneos"][nombre_torneo]["fecha-inicio"] == fecha_torneo[0]:
                    print(f"El torneo '{nombre_torneo}' ya existe en el JSON.")
                    return


            # Agregar el nuevo torneo al diccionario principal
            json_torneo.setdefault("torneos", {})[nombre_torneo] = datos_torneo

            archivo.seek(0)

            # Guardar el JSON actualizado
            json.dump(json_torneo, archivo, indent=4, ensure_ascii=False)
            print(f"Datos del torneo '{nombre_torneo}' agregados al JSON.")

    except FileNotFoundError:
        # Si no existe, crear un nuevo diccionario
        json_torneo = {"torneos": {nombre_torneo: datos_torneo}}

        with open('torneos.json', 'w',encoding='utf-8') as archivo:
            # Guardar el nuevo JSON
            json.dump(json_torneo, archivo, indent=4, ensure_ascii=False)
            print(f"Archivo 'torneos.json' creado con los datos del torneo '{nombre_torneo}'.")    

def resultadosAtletas(texto):
    palabras = texto.split()
    indice = palabras.index("FISCALIZA:")+2
    categoriaActual = ""
    if palabras[indice] == "ESTOS":
        indice += 23
    for categoria in categorias:
        if categoria == palabras[indice]:
            categoriaActual = categoria
            print(f"Coincidencia encontrada: {categoria}")
            if palabras[indice+1] == "|||":
                print(f'{"V"*50}')
            else:
                print(f'{"F"*50}')
        else:
            print("Ninguna coincidencia encontrada.")
            pass

def variablesTorneo(texto):
    claves = ["FECHA:","SIGLAS-LUGAR:","PAIS:","ORGANIZA:","FISCALIZA:","|||"]
    variables = []
    
    palabras = texto.split()
    # Buscar las palabras clave "RESULTADOS" o "RESULTADOS DEL"
    if "RESULTADOS" == palabras[0] and "DEL" == palabras[1]:
        indice_inicio = palabras.index("RESULTADOS") + 2
    elif "RESULTADOS" == palabras[0] and "AL" == palabras[1]:
        indice_inicio = palabras.index("RESULTADOS") + 2
    elif "RESULTADOS" == palabras[0] and "A" == palabras[1] and "LOS" == palabras[2]:
        indice_inicio = palabras.index("RESULTADOS") + 3
    elif "RESULTADOS" == palabras[0] and "DEL" != palabras[1]:
        indice_inicio = palabras.index("RESULTADOS") + 1
    else:
        return None  # No se encontraron palabras clave

    for i in claves:
        if i != claves[-1]:
            if i in palabras[indice_inicio:]:
                indice_fin = palabras[indice_inicio:].index(i) + indice_inicio
            else:
                indice_fin = len(palabras)
            
            variables.append(" ".join(palabras[indice_inicio:indice_fin]))
            indice_inicio = indice_fin +1
        else:
            match = re.search(r'FISCALIZA:\s+(\w+)', texto)

            if match:
                palabra_siguiente = match.group(1)
            else:
                print("No se encontró 'FISCALIZA:' en el texto.")

            variables.append(palabra_siguiente)
    fechaMal = variables[1]
    fecha = fechaMal.replace(" ","")
    fecha = fecha.split("-")
    variables[1] = fecha
    return variables