#datosFAM.py
import re
import os
import json
import pandas as pd
categorias = [
    "U12-M","U12-F",
    "U14-M","U14-F",
    "U16-M","U16-F",
    "U17-M","U17-F",
    "U18-M","U18-F",
    "U20-M","U20-F",
    "U23-M","U23-F",
    "MAYORES-M","MAYORES-F",
]

pruebas = [
    "100 ELECTRONICO",
    "200 ELECTRONICO",
    "300 ELECTRONICO",
    "400 ELECTRONICO",
    "600 ELECTRONICO",
    "800 ELECTRONICO",

    "1500 ELECTRONICO",
    "3000 ELECTRONICO",

    "80 C/V ELECTRONICO",
    "100 C/V ELECTRONICO",
    "110 C/V ELECTRONICO",
    "400 C/V ELECTRONICO",

    "ALTO",
    "TRIPLE",
    "LARGO",
]

def guardarJsonYCSVVariables(variables_torneo):
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
    df = pd.DataFrame([{'id': 0,'nombre': nombre_torneo, 'fecha_inicio': fecha_torneo[0], 'fecha_fin': fecha_torneo[1],'siglas_lugar':siglaslugar_torneo,'pais':pais_torneo,'organiza': organiza_torneo,'fiscaliza': fiscaliza_torneo}])
    df.to_csv('torneos.csv', mode='a', index=False, header=not os.path.exists('torneos.csv'))
    # Guardar en JSON
    try:
        with open('torneos.json', 'r+') as archivo:
            json_torneo = json.load(archivo)

            if nombre_torneo in json_torneo.get("torneos", {}):
                if json_torneo["torneos"][nombre_torneo]["fecha-inicio"] == fecha_torneo[0]:
                    #print(f"El torneo '{nombre_torneo}' ya existe en el JSON.")
                    return

            json_torneo.setdefault("torneos", {})[nombre_torneo] = datos_torneo

            archivo.seek(0)
            json.dump(json_torneo, archivo, indent=4, ensure_ascii=False)
            #print(f"Datos del torneo '{nombre_torneo}' agregados al JSON.")

    except FileNotFoundError:
        json_torneo = {"torneos": {nombre_torneo: datos_torneo}}
        with open('torneos.json', 'w', encoding='utf-8') as archivo:
            json.dump(json_torneo, archivo, indent=4, ensure_ascii=False)
            #print(f"Archivo 'torneos.json' creado con los datos del torneo '{nombre_torneo}'.")    


def resultadosAtletas(texto):
    patron_nombre_fecha = r'\d+\s+([A-Z\s]+)\s+(\d+/\d+\s*/\d+)'
    #print(texto)

    patron_nombre = r'(TORNEO|CAMPEONATO).*?(?=FECHA:)'
    nombre_match = re.finditer(patron_nombre, texto)
    nombre = ""
    for nombre_item in nombre_match:
        for group in nombre_item.groups():
            if group:
                nombre += group + " "
    nombre = nombre.strip()

    patron_fecha = r'FECHA: (\d{2}/\d{2}/\d{4}) - (\d{2}/\d{2}/\d{4})'
    fecha_match = re.search(patron_fecha, texto)
    fecha_inicio = fecha_match.group(1)
    fecha_fin = fecha_match.group(2)

    patron_siglas = r'SIGLAS-LUGAR:\s*(\S+).*?PAIS:'
    siglas_match = re.search(patron_siglas, texto)
    siglas = siglas_match.group(1)
    print("Nombre:",nombre)
    print("Fecha Inicio:",fecha_inicio)
    print("Fecha Fin:",fecha_fin)
    print("Siglas:",siglas)


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
                pass
                #print("No se encontró 'FISCALIZA:' en el texto.")

            variables.append(palabra_siguiente)
    fechaMal = variables[1]
    fecha = fechaMal.replace(" ","")
    fecha = fecha.split("-")
    variables[1] = fecha
    return variables