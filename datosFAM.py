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
                    print(f"El torneo '{nombre_torneo}' ya existe en el JSON.")
                    return

            json_torneo.setdefault("torneos", {})[nombre_torneo] = datos_torneo

            archivo.seek(0)
            json.dump(json_torneo, archivo, indent=4, ensure_ascii=False)
            print(f"Datos del torneo '{nombre_torneo}' agregados al JSON.")

    except FileNotFoundError:
        json_torneo = {"torneos": {nombre_torneo: datos_torneo}}
        with open('torneos.json', 'w', encoding='utf-8') as archivo:
            json.dump(json_torneo, archivo, indent=4, ensure_ascii=False)
            print(f"Archivo 'torneos.json' creado con los datos del torneo '{nombre_torneo}'.")    


def resultadosAtletas(texto):
    patron_nombre_fecha = r'\d+\s+([A-Z\s]+)\s+(\d+/\d+\s*/\d+)'

# Buscar coincidencias en el texto
    coincidencias_nombre_fecha = re.findall(patron_nombre_fecha, texto)

    # Lista para almacenar los registros de los atletas
    atletas = []

    # Iterar sobre las coincidencias y crear un registro para cada atleta
    for coincidencia in coincidencias_nombre_fecha:
        nombre = coincidencia[0].strip()
        fecha_nacimiento = coincidencia[1]
        atleta = {'Nombre': nombre, 'Fecha de nacimiento': fecha_nacimiento}
        atletas.append(atleta)

    # Crear un DataFrame de Pandas a partir de la lista de atletas
    df_atletas = pd.DataFrame(atletas)

    # Imprimir el DataFrame
    print(df_atletas)

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
                prueba = ""
                serie = ""
                palabra_sf = ""

                # Bandera para indicar si se ha encontrado ":" o una palabra que comienza con "S" o "F"
                encontrado = False

                # Recorrer las palabras a partir de la posición siguiente al "|||"
                for i, palabra in enumerate(palabras[indice + 1:]):
                    if encontrado:

                        if palabras[palabras.index(palabra) -2] == ":":
                            print(palabras[palabras.index(palabra) + -2])
                            if palabras[palabras.index(palabra) + 1].startswith(("SERIE", "FINAL")):
                                palabra_sf = palabras[palabras.index(palabra) + 1]
                            elif palabras[palabras.index(palabra) + 2].startswith(("SERIE", "FINAL")):
                                palabra_sf = palabras[palabras.index(palabra) + 2]
                            print("PUNTO---")
                            break
                        elif palabras[palabras.index(palabra) + 5].startswith(("SERIE", "FINAL")):
                            print("FINAL---")
                            palabra_sf = palabra
                            break
                    elif palabra == ":" or palabra.startswith(("SERIE", "FINAL")):
                        encontrado = True
                    else:
                        prueba += palabra + " "
                        prueba = prueba.replace("|||","")

                # Eliminar el espacio final, si es necesario
                prueba = prueba.strip()

                # Imprimir los resultados
                print("Prueba:", prueba)
                print("Serie:", serie)
                print("Palabra con S o F:", palabra_sf)

            else:
                print(f'{"!#$%&/()"*5}')
        else:
            #print("Ninguna coincidencia encontrada.")
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