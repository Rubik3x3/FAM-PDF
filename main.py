import os
import PyPDF2
import re
import json
import glob

import textoFAM
import datosFAM
import extrasFAM

carpeta_pdfs = "PDFs/2023"
archivos_pdf = glob.glob(os.path.join(carpeta_pdfs, "*.pdf"))

categorias = ["U12-M","U12-F","U14-M","U14-F","U16-M","U16-F","U18-M","U18-F","U20-M","U20-F","U23-M","U23-F","MAYORES-M","MAYORES-F",]

json_torneo = {}

def main():
    for archivo_pdf in archivos_pdf:
        generarTextos(archivo_pdf)
        obtenerDatos()

def generarTextos(pdf):
    texto_definitivo = str("")
    texto_definitivo = textoFAM.convertirATexto(pdf)
    texto_definitivo = textoFAM.eliminarEspacios(texto_definitivo)
    textoFAM.duplicarDocumento('TEXTOS/Texto-Sin-Espacios-MAYUS.txt',"TEXTOS/FINAL.txt")
    textoFAM.reemplazarCaracter("TEXTOS/FINAL.txt","_______________________________________________________________________________________________________","|||")
    extrasFAM.textoFinalizoTarea("GENERAR TEXTOS","-",30)

def obtenerDatos():
    with open("TEXTOS/FINAL.txt", 'r') as archivo:
        contenido = archivo.read()
    variables_torneo = datosFAM.variablesTorneo(contenido)
    datosFAM.guardarJsonVariables(variables_torneo)
    extrasFAM.textoFinalizoTarea("OBTENER VARIABLES","-",30)

if __name__ == "__main__":
    main()
    print(json_torneo)
